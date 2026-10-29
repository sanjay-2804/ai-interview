import os
import json
import logging
import httpx
from typing import Dict, Any, List, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

class AIService:
    @property
    def is_configured(self) -> bool:
        return bool(settings.AI_API_KEY and len(settings.AI_API_KEY.strip()) > 5)

    @property
    def provider_name(self) -> str:
        if self.is_configured:
            return f"Live AI ({settings.AI_PROVIDER or 'Gemini'})"
        return "Deterministic Placement Rubric"

    async def evaluate_interview_response(
        self,
        question: str,
        expected_aspects: List[str],
        student_response: str,
        category: str,
        target_role: str
    ) -> Dict[str, Any]:
        """
        Evaluates a student's mock interview response.
        If AI_API_KEY is configured, calls live Gemini API.
        Otherwise, uses strict semantic rubric matching with comprehensive feedback.
        """
        student_text = student_response.strip()
        word_count = len(student_text.split())

        if self.is_configured:
            try:
                ai_result = await self._call_gemini_interview_eval(
                    question, expected_aspects, student_response, category, target_role
                )
                if ai_result:
                    return ai_result
            except Exception as e:
                logger.warning(f"Live AI evaluation failed, falling back to rule engine: {e}")

        # Deterministic / Semantic Rubric Evaluation
        return self._evaluate_with_rubric(question, expected_aspects, student_text, word_count, category)

    async def review_resume(self, resume_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluates resume structure, keywords, completeness, and ATS readiness.
        """
        if self.is_configured:
            try:
                ai_result = await self._call_gemini_resume_review(resume_data)
                if ai_result:
                    return ai_result
            except Exception as e:
                logger.warning(f"Live AI resume review failed, falling back to rule engine: {e}")

        return self._evaluate_resume_rubric(resume_data)

    def _evaluate_with_rubric(
        self,
        question: str,
        expected_aspects: List[str],
        student_text: str,
        word_count: int,
        category: str
    ) -> Dict[str, Any]:
        lower_response = student_text.lower()
        matched_aspects = []
        missing_aspects = []

        for aspect in expected_aspects:
            # Check keywords in aspect
            aspect_words = [w.lower().strip(".,;:?!()") for w in aspect.split() if len(w) > 3]
            match_found = any(word in lower_response for word in aspect_words)
            if match_found:
                matched_aspects.append(aspect)
            else:
                missing_aspects.append(aspect)

        # Base scoring calculation
        if word_count < 10:
            score = 3.0
            strengths = ["Attempted to answer the prompt directly."]
            improvements = ["Provide a complete answer with explanations, examples, and trade-offs rather than a single sentence."]
        else:
            ratio = len(matched_aspects) / max(len(expected_aspects), 1)
            raw_score = 4.0 + (ratio * 5.0)
            if word_count > 40:
                raw_score += 0.5
            if word_count > 80:
                raw_score += 0.5
            score = min(round(raw_score, 1), 9.5)

            strengths = []
            if matched_aspects:
                strengths.append(f"Covered key concepts: {', '.join(matched_aspects[:3])}.")
            if word_count >= 35:
                strengths.append("Structured response with adequate technical depth.")
            else:
                strengths.append("Concisely addressed the central idea.")

            improvements = []
            if missing_aspects:
                improvements.append(f"Consider touching on: {', '.join(missing_aspects[:3])}.")
            improvements.append("Use the STAR method (Situation, Task, Action, Result) for behavioral answers or state time/space complexity for technical topics.")

        sample_answer = self._generate_sample_answer(question, category, expected_aspects)

        return {
            "score": score,
            "evaluation_status": "evaluated",
            "strengths": strengths,
            "missing_concepts": missing_aspects if missing_aspects else ["None observed — all primary concepts covered!"],
            "improvement_suggestions": improvements,
            "sample_answer": sample_answer,
            "ai_engine": self.provider_name
        }

    def _evaluate_resume_rubric(self, resume_data: Dict[str, Any]) -> Dict[str, Any]:
        score = 60
        strengths = []
        improvements = []
        keyword_suggestions = []

        summary = resume_data.get("summary", "") or ""
        skills = resume_data.get("skills_json", []) or []
        projects = resume_data.get("projects_json", []) or []
        education = resume_data.get("education_json", []) or []
        experience = resume_data.get("experience_json", []) or []

        if len(summary.strip()) >= 50:
            score += 8
            strengths.append("Clear career summary highlighting your technical foundation.")
        else:
            improvements.append("Expand your summary to 2-3 sentences specifying your core technologies and career focus.")

        if len(skills) >= 6:
            score += 10
            strengths.append(f"Solid technical skills inventory ({len(skills)} skills listed).")
        else:
            improvements.append("List at least 6-8 core technical competencies including languages, frameworks, and databases.")

        if len(projects) >= 2:
            score += 12
            strengths.append(f"Includes {len(projects)} technical projects showing practical application.")
        else:
            improvements.append("Add at least 2 full-stack, data, or systems projects with GitHub links and measurable results.")

        if len(education) >= 1:
            score += 5
            strengths.append("Education history clearly documented.")
        else:
            improvements.append("Include your degree, institution name, CGPA/percentage, and graduation year.")

        if len(experience) >= 1:
            score += 5
            strengths.append("Includes internship or work experience.")
        else:
            improvements.append("If you have completed internships, open-source contributions, or campus leadership roles, add them to stand out.")

        keyword_suggestions = [
            "REST API", "Database Optimization", "CI/CD", "Unit Testing",
            "Agile/Scrum", "Git Version Control", "System Architecture"
        ]

        return {
            "score": min(score, 95),
            "strengths": strengths,
            "improvements": improvements,
            "keyword_suggestions": keyword_suggestions,
            "engine": self.provider_name
        }

    def _generate_sample_answer(self, question: str, category: str, expected_aspects: List[str]) -> str:
        aspects_str = ", ".join(expected_aspects)
        return (
            f"A high-scoring answer clearly articulates the core definition, illustrates with a real-world scenario, "
            f"and highlights key considerations such as {aspects_str}. "
            f"In an interview, start with a 1-sentence definition, walk through how it works under the hood, and state practical advantages and trade-offs."
        )

    async def _call_gemini_interview_eval(
        self,
        question: str,
        expected_aspects: List[str],
        student_response: str,
        category: str,
        target_role: str
    ) -> Optional[Dict[str, Any]]:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.AI_MODEL or 'gemini-1.5-flash'}:generateContent?key={settings.AI_API_KEY}"
        system_prompt = (
            "You are an expert technical interviewer and placement mentor. "
            "Evaluate the student's answer constructively, fairly, and professionally. "
            "Return valid JSON ONLY with this schema: "
            "{\"score\": float (1-10), \"strengths\": [str], \"missing_concepts\": [str], \"improvement_suggestions\": [str], \"sample_answer\": str}"
        )
        user_prompt = (
            f"Target Role: {target_role}\nCategory: {category}\nQuestion: {question}\n"
            f"Key expected aspects: {', '.join(expected_aspects)}\n"
            f"Student Answer: {student_response}\n\n"
            "Evaluate the answer. Remember to return raw JSON only."
        )

        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": f"{system_prompt}\n\n{user_prompt}"}]}
            ],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json"
            }
        }

        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                parsed = json.loads(text)
                parsed["evaluation_status"] = "evaluated"
                parsed["ai_engine"] = "Live AI (Gemini)"
                return parsed
        return None

    async def _call_gemini_resume_review(self, resume_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.AI_MODEL or 'gemini-1.5-flash'}:generateContent?key={settings.AI_API_KEY}"
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{
                        "text": (
                            "Review this college placement resume. Return JSON ONLY with: "
                            "{\"score\": int (0-100), \"strengths\": [str], \"improvements\": [str], \"keyword_suggestions\": [str]}.\n\n"
                            f"Resume data:\n{json.dumps(resume_data)}"
                        )
                    }]
                }
            ],
            "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"}
        }
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                parsed = json.loads(text)
                parsed["engine"] = "Live AI (Gemini)"
                return parsed
        return None

ai_service = AIService()

