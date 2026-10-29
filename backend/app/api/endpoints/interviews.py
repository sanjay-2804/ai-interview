from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from app.core.database import get_db
from app.models.models import User, InterviewSession
from app.schemas.schemas import (
    MockInterviewStart, MockInterviewDetail
)
from app.api.deps import get_current_user, get_optional_current_user
from app.services.interview_service import interview_service

router = APIRouter(prefix="/interviews", tags=["Mock Interview Centre"])

class ResponseSubmitBody(BaseModel):
    response_text: str

@router.post("/sessions", response_model=MockInterviewDetail)
def start_interview_session(
    payload: MockInterviewStart,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return interview_service.start_interview(
        db=db,
        user_id=current_user.id,
        category=payload.category,
        target_role=payload.target_role,
        difficulty=payload.difficulty,
        question_count=payload.question_count
    )

@router.get("/sessions")
def list_interview_sessions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    sessions = db.query(InterviewSession).filter(
        InterviewSession.user_id == current_user.id
    ).order_by(InterviewSession.created_at.desc()).all()

    return [
        {
            "id": s.id,
            "category": s.category,
            "target_role": s.target_role,
            "difficulty": s.difficulty,
            "total_questions": s.total_questions,
            "completed_questions": s.completed_questions,
            "overall_score": s.overall_score,
            "status": s.status,
            "feedback_summary": s.feedback_summary,
            "created_at": s.created_at.strftime("%b %d, %Y")
        } for s in sessions
    ]

@router.get("/sessions/{session_id}", response_model=MockInterviewDetail)
def get_interview_session(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return interview_service.get_interview(db, session_id, current_user.id)

@router.post("/sessions/{session_id}/responses", response_model=MockInterviewDetail)
async def submit_session_response(
    session_id: int,
    payload: ResponseSubmitBody,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return await interview_service.submit_response(
        db=db,
        session_id=session_id,
        user_id=current_user.id,
        response_text=payload.response_text
    )

@router.get("/sessions/{session_id}/feedback")
def get_interview_feedback(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session = interview_service.get_interview(db, session_id, current_user.id)
    return {
        "session_id": session.id,
        "overall_score": session.overall_score,
        "feedback_summary": session.feedback_summary,
        "responses": session.responses
    }

@router.get("/hr-questions")
def get_hr_star_questions():
    return [
        {
            "id": 1,
            "category": "Team Conflict & Collaboration",
            "question": "Tell me about a time when you had a serious disagreement with a project team member. How did you handle it?",
            "competency": "Conflict Resolution & Emotional Intelligence",
            "star_breakdown": {
                "situation": "During our final semester capstone project, our 4-person team had to choose between PostgreSQL and MongoDB for our user analytics service.",
                "task": "A teammate insisted on MongoDB due to rapid JSON prototyping, whereas our schema had tightly coupled relational integrity that required ACID guarantees.",
                "action": "Rather than arguing hypotheticals, I scheduled a 30-minute benchmarking spike. We wrote a quick mock script testing 50,000 multi-table relational joins on both databases. The data demonstrated PostgreSQL maintained strict referential integrity and ran 40% faster on relational queries. I also integrated JSONB columns in Postgres so my teammate could still store unstructured metadata easily.",
                "result": "My teammate agreed with the evidence-based decision, and we delivered the project 1 week early with zero database corruption bugs."
            },
            "sample_answer": "In our college capstone project, our team was divided between choosing PostgreSQL or MongoDB. Instead of debating personal preferences, I proposed an objective benchmarking spike where we tested 50,000 sample joins. When the data revealed PostgreSQL had 40% lower query latency and preserved relational integrity, we adopted it while utilizing Postgres JSONB fields to accommodate my teammate's unstructured data needs. This led to an early, error-free project submission.",
            "common_mistakes": "Saying 'I never have conflicts' (shows lack of experience or self-awareness), blaming the teammate, or yielding without discussing technical trade-offs."
        },
        {
            "id": 2,
            "category": "Overcoming Failure & Resilience",
            "question": "Describe a major technical failure or mistake you made. What happened and what did you learn?",
            "competency": "Accountability & Continuous Learning",
            "star_breakdown": {
                "situation": "During an internship assignment, I pushed a database schema change directly to the staging server without backing up the active mock dataset.",
                "task": "A column migration failed halfway, locking the database table and breaking QA automated test suites for the entire afternoon.",
                "action": "I immediately took ownership of the error, notified my team lead on Slack, and executed a rollback script from our versioned migration files within 25 minutes. To prevent recurrence, I configured an automated pre-migration backup hook in our CI/CD pipeline.",
                "result": "The staging server was restored, and my automated backup hook became a standard checklist item for all subsequent developer deployments."
            },
            "sample_answer": "Early in my internship, I executed a migration on our staging database that failed mid-way, halting QA testing. Rather than hiding the issue, I alerted the team immediately and restored the database within 25 minutes using Alembic rollback files. Afterwards, I wrote a CI pre-migration validation script that verifies schema rollbacks before any deployment. This taught me that proactive transparency and automated guardrails are fundamental to production engineering.",
            "common_mistakes": "Choosing a fake failure ('I work too hard'), shifting blame to tools or managers, or failing to highlight the preventative measures implemented."
        },
        {
            "id": 3,
            "category": "Ambiguity & Tight Deadlines",
            "question": "How do you prioritize your work when given multiple urgent tasks with unclear requirements?",
            "competency": "Prioritization & Decisiveness",
            "star_breakdown": {
                "situation": "During midterm exams week, our hackathon team had 24 hours remaining to complete our submission while two key API specifications were incomplete.",
                "task": "I had to balance preparing for my exam while delivering our core authentication and payment integration workflows.",
                "action": "I created an Eisenhower matrix to distinguish urgent vs important features. I stubbed the missing external APIs using mock JSON fixtures, unblocking our frontend team while I studied for my exam, and scheduled a 10-minute sync with the organizer to clarify the API payload specs.",
                "result": "We passed our exams and won second place at the hackathon, finishing all core demo workflows on time."
            },
            "sample_answer": "When facing tight deadlines with ambiguity, I break work into high-impact core requirements versus secondary enhancements. I create mock contracts for unconfirmed APIs so team progress never halts, proactively seek targeted clarification from stakeholders, and deliver a working vertical slice before expanding scope.",
            "common_mistakes": "Panicking, guessing requirements without confirming with stakeholders, or working on trivial details while core deliverables are stalled."
        }
    ]

# --- Company-Specific Placement Drives Endpoints ---

from app.services.company_interview_service import company_service

@router.get("/companies")
def list_company_drives():
    return company_service.list_companies()

@router.get("/companies/{slug}")
def get_company_drive_detail(slug: str):
    comp = company_service.get_company(slug)
    if not comp:
        raise HTTPException(status_code=404, detail="Company drive specification not found.")
    return comp

class CompanyRoundEvalRequest(BaseModel):
    round_number: int
    question: str
    student_response: str

@router.post("/companies/{slug}/evaluate-round")
async def evaluate_company_round(
    slug: str,
    payload: CompanyRoundEvalRequest,
    current_user: Optional[User] = Depends(get_optional_current_user),
    db: Session = Depends(get_db)
):
    comp = company_service.get_company(slug)
    if not comp:
        raise HTTPException(status_code=404, detail="Company not found.")
    
    round_info = next((r for r in comp["rounds"] if r["round_number"] == payload.round_number), None)
    if not round_info:
        raise HTTPException(status_code=404, detail="Round number not found for company.")
    
    # Check if this was a known MCQ question
    matched_q = None
    payload_q_norm = "".join(payload.question.split()).lower()
    for sq in round_info.get("sample_questions", []):
        sq_norm = "".join(sq.get("question", "").split()).lower()
        if sq_norm == payload_q_norm or sq_norm in payload_q_norm or payload_q_norm in sq_norm:
            matched_q = sq
            break

    cutoff = round_info.get("cutoff_percentage", 65)

    if matched_q and "options" in matched_q and "answer" in matched_q:
        student_ans = payload.student_response.strip().lower()
        correct_ans = matched_q["answer"].strip().lower()
        is_correct = (student_ans == correct_ans) or (student_ans in correct_ans and len(student_ans) > 2)

        final_score = 100 if is_correct else 35
        cleared = final_score >= cutoff
        verdict = "CORRECT ANSWER - ROUND CLEARED" if is_correct else f"INCORRECT (Correct: {matched_q['answer']})"
        feedback = f"Official Solution: {matched_q.get('explanation', '')}"
    else:
        ans_len = len(payload.student_response.split())
        base_score = 65
        if ans_len >= 25:
            base_score += 15
        if ans_len >= 50:
            base_score += 10
        
        keywords = ["complexity", "o(n)", "acid", "algorithm", "database", "star", "result", "action", "project", "optimization", "greedy", "dp"]
        matched = [kw for kw in keywords if kw in payload.student_response.lower()]
        keyword_bonus = min(10, len(matched) * 3)
        final_score = min(96, base_score + keyword_bonus)
        cleared = final_score >= cutoff
        verdict = "ROUND CLEARED - RECOMMEND FOR NEXT ROUND" if cleared else "BORDERLINE - REVIEW REQUIRED"
        feedback = f"Response demonstrates structured reasoning and aligns with {comp['name']} standards for {round_info['name']}."

    return {
        "company_name": comp["name"],
        "round_name": round_info["name"],
        "score": final_score,
        "cutoff_required": cutoff,
        "cleared_round": cleared,
        "verdict": verdict,
        "feedback": feedback,
        "improvement_tips": round_info.get("tips", "Focus on time-space complexity and structured STAR answers.")
    }

class CompanyAddQuestionRequest(BaseModel):
    round_number: int = 1
    question: str
    options: Optional[List[str]] = None
    answer: Optional[str] = None
    explanation: Optional[str] = None
    expected: Optional[List[str]] = None
    model_answer: Optional[str] = None

class CompanyAskAIRequest(BaseModel):
    company_slug: str
    round_number: Optional[int] = 1
    question: str
    student_notes: Optional[str] = None

@router.post("/companies/{slug}/questions")
def add_company_question(
    slug: str,
    payload: CompanyAddQuestionRequest,
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    comp = company_service.get_company(slug)
    if not comp:
        raise HTTPException(status_code=404, detail="Company not found.")
    
    q_data = {
        "question": payload.question.strip()
    }
    if payload.options:
        q_data["options"] = payload.options
    if payload.answer:
        q_data["answer"] = payload.answer
    if payload.explanation:
        q_data["explanation"] = payload.explanation
    if payload.expected:
        q_data["expected"] = payload.expected
    if payload.model_answer:
        q_data["model_answer"] = payload.model_answer

    success = company_service.add_question(slug, payload.round_number, q_data)
    if not success:
        raise HTTPException(status_code=400, detail="Could not add question to specified round.")
    
    return {
        "message": f"Question added successfully to {comp['name']} Round {payload.round_number}!",
        "company": comp["name"],
        "round_number": payload.round_number
    }

@router.post("/companies/ask-ai")
def ask_company_ai(payload: CompanyAskAIRequest):
    comp = company_service.get_company(payload.company_slug)
    comp_name = comp["name"] if comp else "Premier Tech Employer"
    
    q_lower = payload.question.lower()
    
    is_dsa = any(k in q_lower for k in ["tree", "graph", "dp", "dynamic programming", "array", "pointer", "sort", "heap", "stack", "queue", "search", "complexity", "o(n)"])
    is_design = any(k in q_lower for k in ["system", "design", "scale", "database", "cache", "redis", "kafka", "microservice", "rate limit", "sharding", "acid"])
    is_hr = any(k in q_lower for k in ["why", "conflict", "tell me about", "weakness", "deadline", "star", "failure", "relocate", "values"])
    
    if is_dsa:
        category = "Data Structures & Algorithmic Complexity"
        concept = "Algorithmic Efficiency & Edge-Case Handling"
        rubric = f"At {comp_name}, interviewers evaluate optimal Time/Space complexity (O(N) or O(log N)), proactive edge-case boundary checks (empty inputs, nulls, negative numbers), and modular clean code."
        model_answer = (
            f"1. Clarify constraints (input size N, memory limits).\n"
            f"2. State brute force approach and its complexity trade-offs.\n"
            f"3. Propose optimal approach using proper data structures (Hash Map / Two Pointers / Heap).\n"
            f"4. Walk through with a small test input trace.\n"
            f"5. Explicitly state final Time and Auxiliary Space complexity."
        )
        follow_ups = [
            f"How would your algorithm scale if the dataset exceeded available RAM (External Memory / Streaming)?",
            f"What happens if there are duplicate or negative values in the input?",
            f"Can we optimize auxiliary space complexity from O(N) to O(1) in-place?"
        ]
    elif is_design:
        category = "System Architecture & High-Scale Reliability"
        concept = "Distributed Scalability & Fault Tolerance"
        rubric = f"At {comp_name}, system design rounds test your ability to decompose problems into services, balance the CAP theorem, select appropriate storage tiers (SQL vs NoSQL), and introduce caching (Redis/CDN) without creating single points of failure."
        model_answer = (
            f"1. Scope Functional & Non-Functional Requirements (QPS, Read:Write ratio, Availability target 99.99%).\n"
            f"2. High-Level Diagram: API Gateway -> Load Balancer -> Stateless App Services -> Cache Tier (Redis) -> Primary/Replica DB.\n"
            f"3. Data Model & Partitioning: Consistent hashing on user_id to avoid hot partitions.\n"
            f"4. Reliability: Asynchronous messaging via Kafka for decoupling and Token Bucket rate limiting."
        )
        follow_ups = [
            f"How do you handle a cache stampede (thundering herd) during peak flash sales?",
            f"What is your disaster recovery and multi-region replication strategy?",
            f"How do you monitor and alert on latency spikes (P99 latency > 200ms)?"
        ]
    elif is_hr:
        category = "Behavioral & Culture Alignment"
        concept = "Leadership, Ownership & STAR Communication"
        rubric = f"At {comp_name}, recruiters look for the STAR method: clear Situation, specific Task, your own individual Action (not just 'we did'), and measurable Result with lessons learned."
        model_answer = (
            f"Situation: Set clear technical context and challenge.\n"
            f"Task: Your explicit engineering responsibility.\n"
            f"Action: Step-by-step proactive decisions taken, tools utilized, and how you engaged stakeholders.\n"
            f"Result: Quantifiable metric (e.g., 'reduced API latency by 35% and delivered 4 days ahead of schedule')."
        )
        follow_ups = [
            f"What would you do differently if you faced that exact situation again today?",
            f"How did this experience shape your engineering principles and team collaboration style?",
            f"How do you measure success when working on ambiguous requirements?"
        ]
    else:
        category = "Technical Fundamentals & Problem Solving"
        concept = "Core CS Depth & Practical Application"
        rubric = f"At {comp_name}, technical screening tests foundational understanding of OS, DBMS, Networks, and clean OOP architecture."
        model_answer = (
            f"Provide an accurate definition, cite a concrete production use case, contrast with alternative approaches, and explain potential pitfalls to avoid."
        )
        follow_ups = [
            f"What are the major trade-offs of this approach in high-throughput enterprise environments?",
            f"How do you test and debug this in a production CI/CD environment?",
            f"Can you give an example of a failure scenario and how to mitigate it?"
        ]

    return {
        "company_name": comp_name,
        "question": payload.question,
        "category": category,
        "core_concept": concept,
        "recruiter_grading_rubric": rubric,
        "model_answer": model_answer,
        "follow_up_questions": follow_ups
    }

