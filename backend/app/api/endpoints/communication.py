import re
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.models import User, CommunicationSession, ActivityEvent, utc_now
from app.schemas.schemas import CommunicationSubmitRequest, CommunicationSessionOut

router = APIRouter(prefix="/communication", tags=["communication"])

# Curated Prompts across all key categories
PROMPTS = [
    {
        "id": 1,
        "title": "Tell Me About Yourself",
        "category": "Self Introduction",
        "question": "Walk me through your academic background, core programming focus, key project or internship, and why you are excited about software engineering.",
        "framework": "Present, Past, Future: 1. Current studies & core focus -> 2. Hands-on impact -> 3. Why this company aligns with your trajectory.",
        "target_duration_seconds": 90,
        "sample_answer": "I am a final-year Computer Science undergraduate specializing in full-stack web systems and algorithmic problem solving. Over the past year, I built InterviewAI, a placement preparation platform using FastAPI and React that evaluated code efficiency and simulated technical rounds. During my internship at TechInnovate, I optimized database queries reducing latency by 35%. I am eager to apply my background in scalable APIs and high-availability design to your backend engineering team."
    },
    {
        "id": 2,
        "title": "Why Should We Hire You?",
        "category": "Value Proposition",
        "question": "What sets you apart from other qualified campus candidates applying for this engineering position?",
        "framework": "Unique Value Proposition: Technical fundamentals + Rapid self-learning agility + Culture fit and ownership mindset from Day 1.",
        "target_duration_seconds": 75,
        "sample_answer": "Beyond having strong fundamentals in data structures, SQL, and clean code, what differentiates me is my engineering curiosity and bias for shipping working software. I don't just learn syntax; I build end-to-end applications, test edge cases, and read documentation. I am excited about your engineering challenges in distributed systems and ready to contribute immediately with high ownership."
    },
    {
        "id": 3,
        "title": "Conflict Resolution & Teamwork",
        "category": "Behavioral / STAR",
        "question": "Describe a situation where you had a major disagreement with a team member regarding a technical decision. How did you resolve it?",
        "framework": "STAR Method: Situation -> Task -> Action (objective benchmarking, listening) -> Result (consensus, on-time delivery).",
        "target_duration_seconds": 90,
        "sample_answer": "In our 4-person capstone project, our frontend developer wanted to use MongoDB while I advocated for PostgreSQL. Rather than arguing, I proposed building a quick benchmark for our relational queries involving complex JOINs. The benchmark showed PostgreSQL had 40% lower response times for our schema, and our team unanimously agreed. We finished the project 2 weeks ahead of schedule with zero data anomalies."
    },
    {
        "id": 4,
        "title": "Explain a Technical Concept to a Beginner",
        "category": "Technical Explanation",
        "question": "Explain what an API is and why software systems use them, using a real-world non-technical analogy.",
        "framework": "Analogy -> Definition -> Technical Example -> Value Proposition.",
        "target_duration_seconds": 75,
        "sample_answer": "Think of an API like a waiter in a restaurant. You are the customer, and the kitchen is the system preparing the food. You don't walk into the kitchen to cook; you look at the menu, tell the waiter your order, and the waiter brings back your meal. In software, an API allows an app like Uber to request map data from Google Maps without needing to build satellite navigation from scratch."
    },
    {
        "id": 5,
        "title": "Describe a Challenging Bug You Solved",
        "category": "Technical Problem Solving",
        "question": "Tell me about a difficult bug or performance issue you encountered in your code. How did you diagnose and resolve it?",
        "framework": "Symptom -> Systematic Debugging Steps -> Root Cause -> Solution -> Prevention.",
        "target_duration_seconds": 90,
        "sample_answer": "While building a real-time chat application, messages were sporadically duplicating. Instead of guessing, I inspected network websockets and database logs. I discovered the frontend was registering duplicate event listeners on component re-mounts. I added a cleanup function in the useEffect hook and introduced idempotency keys on the backend, completely eliminating duplicate message records."
    },
    {
        "id": 6,
        "title": "What Are Your Strengths and Weaknesses?",
        "category": "Self Awareness",
        "question": "Identify one genuine technical or work-style strength and one area of growth you are actively working to improve.",
        "framework": "Strength with Evidence -> Genuine Growth Area -> Active Concrete Remediation.",
        "target_duration_seconds": 75,
        "sample_answer": "My primary strength is systematic problem decomposition: when faced with ambiguous requirements, I break them into modular milestones and write unit tests first. An area I am actively improving is delegating tasks in group settings; in the past, I tended to take on extra workload to ensure deadlines were met. Recently, I started utilizing Kanban boards and daily check-ins, which has significantly improved our team's shared accountability."
    }
]

FILLER_WORDS = [
    r"\bum\b", r"\buh\b", r"\bah\b", r"\blike\b", r"\bbasically\b",
    r"\byou know\b", r"\bactually\b", r"\bsort of\b", r"\bkind of\b",
    r"\bi mean\b", r"\bso yeah\b", r"\bliterally\b"
]

def analyze_transcript(
    transcript: str,
    duration_seconds: float,
    prompt_question: str,
    framework: Optional[str]
) -> dict:
    text = transcript.strip()
    words = text.split()
    word_count = len(words)
    
    # Estimate duration if 0
    effective_duration = duration_seconds if duration_seconds > 5 else max(15.0, (word_count / 130.0) * 60.0)
    wpm = int((word_count / (effective_duration / 60.0))) if effective_duration > 0 else 125

    # Filler words detection
    fillers_found = []
    text_lower = text.lower()
    for filler_regex in FILLER_WORDS:
        matches = re.findall(filler_regex, text_lower)
        if matches:
            fillers_found.extend(matches)
    
    filler_count = len(fillers_found)

    # 1. Relevance Score (25% weight)
    question_keywords = set(re.findall(r"\w{4,}", prompt_question.lower()))
    transcript_words = set(re.findall(r"\w{4,}", text_lower))
    overlap = len(question_keywords.intersection(transcript_words))
    relevance_score = min(9.5, max(5.0, 6.0 + (overlap * 0.6)))

    # 2. Clarity & Organization (25% weight)
    # Check for transition words (first, then, because, as a result, for example, finally)
    transitions = ["first", "second", "then", "because", "result", "for example", "furthermore", "finally", "specifically", "however"]
    trans_count = sum(1 for t in transitions if t in text_lower)
    clarity_score = min(9.5, max(5.5, 6.5 + (trans_count * 0.5)))

    # 3. Grammar & Vocabulary (20% weight)
    # Penalize very short words, reward varied vocabulary
    unique_words_ratio = (len(set(words)) / max(1, word_count))
    grammar_score = min(9.5, max(5.0, 5.5 + (unique_words_ratio * 4.0)))

    # 4. Conciseness & Structure (15% weight)
    if 40 <= word_count <= 250:
        conciseness_score = 9.0
    elif word_count < 40:
        conciseness_score = 5.5
    else:
        conciseness_score = 7.0

    # 5. Delivery Measures (WPM & Fillers) (15% weight)
    # Optimal speaking rate is 120-160 WPM
    if 115 <= wpm <= 165:
        wpm_score = 9.0
    elif 90 <= wpm < 115 or 165 < wpm <= 190:
        wpm_score = 7.5
    else:
        wpm_score = 6.0

    # Filler penalty
    filler_ratio = filler_count / max(1, word_count)
    if filler_ratio < 0.02:
        filler_score = 9.5
    elif filler_ratio < 0.05:
        filler_score = 8.0
    else:
        filler_score = 6.0

    delivery_score = round((wpm_score * 0.6) + (filler_score * 0.4), 1)

    # Overall Weighted Score (out of 10)
    overall_score = round(
        (relevance_score * 0.25) +
        (clarity_score * 0.25) +
        (grammar_score * 0.20) +
        (conciseness_score * 0.15) +
        (delivery_score * 0.15),
        1
    )

    # Strengths
    strengths = []
    if relevance_score >= 7.5:
        strengths.append("High contextual relevance to the interviewer's prompt.")
    if clarity_score >= 7.5:
        strengths.append("Clear structural flow with well-placed transitional reasoning.")
    if wpm >= 115 and wpm <= 165:
        strengths.append(f"Optimal conversational cadence ({wpm} WPM) indicating poise.")
    if filler_count <= 1:
        strengths.append("Exceptional command of speech with minimal filler words.")
    if len(strengths) == 0:
        strengths.append("Good initial foundation; clear intent and conversational confidence.")

    # Actionable Improvements
    improvements = []
    if filler_count >= 2:
        improvements.append(f"Reduce filler word frequency ({filler_count} detected: {', '.join(set(fillers_found))}). Replace filler sounds with a deliberate 1-second pause.")
    if wpm < 115:
        improvements.append(f"Speaking rate is slightly measured ({wpm} WPM). Aim for 130-150 WPM to project confident enthusiasm.")
    elif wpm > 165:
        improvements.append(f"Pacing was rapid ({wpm} WPM). Slow down at key technical outcomes so the interviewer absorbs the impact.")
    if word_count < 45:
        improvements.append("Expand your answer with a concrete metric, benchmark, or business result.")
    if clarity_score < 7.5:
        improvements.append("Use structured signposting: 'First, the technical challenge was... Second, our action was... Finally, the outcome was...'")
    if len(improvements) == 0:
        improvements.append("Polish delivery by practicing in front of a mirror to ensure open body language and eye contact.")

    # Personalized Concept Extraction based on student's actual response
    tech_terms = [
        "python", "java", "javascript", "c++", "sql", "react", "fastapi", "django", "node",
        "docker", "kubernetes", "postgresql", "mongodb", "redis", "aws", "git", "api", "rest",
        "microservices", "kafka", "data structures", "algorithms", "dsa", "oop", "system design"
    ]
    detected_tech = [t for t in tech_terms if re.search(r'\b' + re.escape(t) + r'\b', text_lower)]

    concepts_demonstrated = []
    if detected_tech:
        concepts_demonstrated.append(f"Technical Stack Cited: {', '.join([t.title() for t in detected_tech[:4]])}")
    if any(w in text_lower for w in ["first", "then", "finally", "because", "result"]):
        concepts_demonstrated.append("Structured Sequencing: Signposted narrative with cause-and-effect transitions.")
    if any(w in text_lower for w in ["percent", "%", "seconds", "ms", "times", "users", "hours"]):
        concepts_demonstrated.append("Quantifiable Outcomes: Referenced specific metrics or impact measurements.")
    if any(w in text_lower for w in ["project", "internship", "built", "developed", "architected"]):
        concepts_demonstrated.append("Engineering Ownership: Directly articulated hands-on project responsibility.")
    if len(concepts_demonstrated) == 0:
        concepts_demonstrated.append("Conversational clarity and direct answer addressing the core question prompt.")

    concepts_missing = []
    if not any(w in text_lower for w in ["percent", "%", "seconds", "ms", "reduced", "scaled", "metrics", "benchmark"]):
        concepts_missing.append("Measurable Impact: Omitted numerical outcomes (e.g., % improvement, latency reduction, throughput).")
    if not any(w in text_lower for w in ["because", "therefore", "tradeoff", "decided", "chose"]):
        concepts_missing.append("Architectural Justification: Did not explain 'why' a specific technology or design was chosen.")
    if word_count < 45:
        concepts_missing.append("Contextual Depth: Answer length is under 45 words, limiting demonstration of senior competencies.")

    # Targeted Follow-up question based directly on student's actual response
    if detected_tech:
        primary_tech = detected_tech[0].title()
        follow_up_question = f"You highlighted your experience with {primary_tech}. What was the most difficult architectural trade-off or debugging challenge you navigated while using {primary_tech}?"
    elif "conflict" in text_lower or "team" in text_lower:
        follow_up_question = "When handling technical disagreements in a sprint, how do you balance code quality with delivery deadlines?"
    elif "api" in text_lower:
        follow_up_question = "How do you approach API versioning and backward compatibility when external clients consume your service?"
    elif word_count >= 50:
        follow_up_question = "If you had an additional two weeks to iterate on that project, what specific reliability or security enhancements would you prioritize?"
    else:
        follow_up_question = "Can you walk me step-by-step through a concrete technical project where you implemented this approach and what the final outcome was?"

    if detected_tech:
        personalized_coaching = f"Your mention of {', '.join([t.title() for t in detected_tech[:3]])} provides credible engineering context. To make this an exceptional answer, explain the specific trade-offs and metrics behind that technology choice."
    else:
        personalized_coaching = "Ground your verbal explanations in real engineering examples from your GitHub projects or coursework rather than staying strictly theoretical."

    return {
        "overall_score": overall_score,
        "relevance_score": round(relevance_score, 1),
        "clarity_score": round(clarity_score, 1),
        "grammar_score": round(grammar_score, 1),
        "conciseness_score": round(conciseness_score, 1),
        "delivery_score": round(delivery_score, 1),
        "wpm": wpm,
        "filler_words_count": filler_count,
        "filler_words_list": list(set(fillers_found)),
        "strengths": strengths,
        "improvements": improvements,
        "concepts_demonstrated": concepts_demonstrated,
        "concepts_missing": concepts_missing,
        "follow_up_question": follow_up_question,
        "personalized_coaching": personalized_coaching
    }

@router.get("/prompts")
def get_prompts():
    """Return all curated communication and interview speaking prompts."""
    return PROMPTS

@router.post("/submit", response_model=CommunicationSessionOut, status_code=status.HTTP_201_CREATED)
def submit_communication_attempt(
    payload: CommunicationSubmitRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not payload.transcript.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Transcript cannot be empty. Please speak aloud or provide your spoken response."
        )

    # Find matching prompt sample answer if available
    matched_sample = None
    for p in PROMPTS:
        if p["title"].lower() == payload.prompt_title.lower():
            matched_sample = p["sample_answer"]
            break

    analysis = analyze_transcript(
        transcript=payload.transcript,
        duration_seconds=payload.audio_duration_seconds or 0.0,
        prompt_question=payload.prompt_question,
        framework=payload.framework
    )

    session_record = CommunicationSession(
        user_id=current_user.id,
        category=payload.category,
        prompt_title=payload.prompt_title,
        prompt_question=payload.prompt_question,
        framework=payload.framework,
        audio_filename=payload.audio_filename,
        audio_duration_seconds=payload.audio_duration_seconds or 0.0,
        transcript=payload.transcript.strip(),
        overall_score=analysis["overall_score"],
        relevance_score=analysis["relevance_score"],
        clarity_score=analysis["clarity_score"],
        grammar_score=analysis["grammar_score"],
        conciseness_score=analysis["conciseness_score"],
        delivery_score=analysis["delivery_score"],
        wpm=analysis["wpm"],
        filler_words_count=analysis["filler_words_count"],
        filler_words_list=analysis["filler_words_list"],
        strengths=analysis["strengths"],
        improvements=analysis["improvements"],
        concepts_demonstrated=analysis["concepts_demonstrated"],
        concepts_missing=analysis["concepts_missing"],
        follow_up_question=analysis["follow_up_question"],
        personalized_coaching=analysis["personalized_coaching"],
        sample_answer=matched_sample,
        status="completed"
    )

    db.add(session_record)
    db.flush()

    # Log activity event
    event = ActivityEvent(
        user_id=current_user.id,
        event_type="communication_practice",
        title=f"Spoke on: {payload.prompt_title}",
        details=f"Score: {analysis['overall_score']}/10 | Cadence: {analysis['wpm']} WPM | Category: {payload.category}",
        metadata_json={
            "session_id": session_record.id,
            "score": analysis["overall_score"],
            "wpm": analysis["wpm"],
            "fillers": analysis["filler_words_count"]
        }
    )
    db.add(event)
    db.commit()
    db.refresh(session_record)

    return session_record

@router.get("/history", response_model=List[CommunicationSessionOut])
def get_communication_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retrieve the current student's audio speaking practice sessions."""
    return db.query(CommunicationSession)\
        .filter(CommunicationSession.user_id == current_user.id)\
        .order_by(CommunicationSession.created_at.desc())\
        .all()

@router.get("/session/{session_id}", response_model=CommunicationSessionOut)
def get_session_detail(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session_record = db.query(CommunicationSession)\
        .filter(CommunicationSession.id == session_id, CommunicationSession.user_id == current_user.id)\
        .first()
    if not session_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Communication session not found.")
    return session_record

@router.get("/group-discussions")
def get_group_discussions():
    return [
        {
            "id": 1,
            "title": "Artificial Intelligence in Software Engineering: Threat to Junior Devs or Force Multiplier?",
            "category": "Technology & Employment",
            "context": "AI code generation tools (Copilot, ChatGPT, Claude) are rapidly automating boilerplate code. Recruitment panels frequently test freshers' practical perspective on AI vs core software engineering foundations.",
            "opening_statement": "Good morning everyone. The emergence of generative AI in software engineering is undeniably transforming development velocity. Today's discussion centers on whether this shifts junior developers into higher-leverage architects or threatens entry-level employment.",
            "arguments_for": [
                "Automates repetitive CRUD, boilerplate code, and regex generation, saving 30-40% developer time.",
                "Enables single developers to prototype full-stack systems and automated test suites rapidly.",
                "Shifts focus from memorizing syntax to system architecture, debugging, and domain problem solving.",
                "Lowers barrier to entry for cross-disciplinary engineering and AI-assisted pair programming."
            ],
            "arguments_against": [
                "Over-reliance impairs deep fundamental debugging skills and understanding of memory/complexity.",
                "Security vulnerabilities, hallucinated dependencies, and licensing risks introduced into production codebases.",
                "Risk of reducing traditional entry-level hiring quotas if companies expect 1 engineer to do the work of 3.",
                "Junior developers need to struggle through foundational errors to build true engineering intuition."
            ],
            "conclusion_strategy": "Summarize that AI tools will not replace software engineers, but engineers who skillfully wield AI will replace those who do not. Core CS principles (DSA, concurrency, system design) become even more critical to audit AI output.",
            "rubric": {
                "content_depth": "Demonstrates balanced knowledge without being purely alarmist or blindly optimistic.",
                "active_listening": "Acknowledges previous speaker before introducing new dimension.",
                "leadership": "Brings the group back to core topic if conversation wanders into trivia."
            }
        },
        {
            "id": 2,
            "title": "Work from Home (Remote Work) vs Return to Office in Tech Companies",
            "category": "Workplace & Economy",
            "context": "Many tech giants (Amazon, TCS, Infosys) have mandated 5-day office returns while startups champion remote-first culture. Tests candidates' grasp of productivity, team culture, and business reality.",
            "opening_statement": "Hello peers. The debate between remote flexibility and in-office collaboration goes beyond convenience — it touches corporate culture, mentoring of freshers, and long-term organizational throughput.",
            "arguments_for": [
                "In-person whiteboard sessions accelerate spontaneous brainstorming and knowledge transfer.",
                "Junior engineers learn faster through osmosis, informal watercooler discussions, and direct mentorship.",
                "Stronger team bonding, lower attrition, and clearer boundaries between personal life and work.",
                "Prevents data security leaks and unmonitored intellectual property exposure."
            ],
            "arguments_against": [
                "Saves 2-3 hours of grueling daily commute, enhancing work-life balance and mental well-being.",
                "Enables companies to hire global tier-2/tier-3 talent regardless of geographic relocation constraints.",
                "Significantly reduces infrastructure overhead (office leases, electricity, transport costs).",
                "Proven productivity gains for deep, uninterrupted coding and asynchronous engineering."
            ],
            "conclusion_strategy": "Advocate for a balanced hybrid model (e.g. 2-3 days in office for collaborative sprints and design reviews, with remaining days remote for deep focus work).",
            "rubric": {
                "content_depth": "Considers both employee well-being and company business objectives.",
                "moderation": "Maintains calm professional composure during heated debate."
            }
        },
        {
            "id": 3,
            "title": "Data Privacy vs Public Security: Should Encryption Have Government Backdoors?",
            "category": "Ethics & Cybersecurity",
            "context": "Governments frequently demand access to encrypted messaging platforms (WhatsApp, Signal) to investigate criminal syndicates, while privacy advocates argue backdoors weaken global digital infrastructure.",
            "opening_statement": "Friends, encryption is the mathematical bedrock of e-commerce, banking, and digital trust. Today we address the complex tension between national security investigations and individual privacy rights.",
            "arguments_for": [
                "A mathematical backdoor created for law enforcement will inevitably be discovered and exploited by hostile nation-states and cybercriminals.",
                "End-to-end encryption protects human rights, journalists, and corporate trade secrets from mass surveillance.",
                "Weakening encryption damages confidence in digital banking, healthcare records, and national infrastructure."
            ],
            "arguments_against": [
                "Criminal networks and terrorists exploit impenetrable encryption to coordinate operations beyond legal oversight.",
                "Sovereign governments carry the constitutional responsibility to protect citizen safety with court-authorized warrants.",
                "Metadata and lawful intercept frameworks are standard in telecommunications and physical law."
            ],
            "conclusion_strategy": "Highlight that mathematical security cannot distinguish good actors from bad actors. Targeted endpoint lawful forensics under strict judicial warrant should be preferred over weakening systemic encryption algorithms.",
            "rubric": {
                "technical_accuracy": "Understands cryptographic principles (public key cryptography, mathematical hardness)."
            }
        }
    ]

