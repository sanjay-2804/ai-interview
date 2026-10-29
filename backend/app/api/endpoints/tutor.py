from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from app.core.database import get_db
from app.models.models import (
    User, SubmittedAnswer, Question, Topic, CodingSubmission, CommunicationSession
)
from app.api.deps import get_current_user

router = APIRouter(prefix="/tutor", tags=["AI Placement Tutor"])

class TutorChatRequest(BaseModel):
    message: str
    topic_context: Optional[str] = None

class TutorChatResponse(BaseModel):
    reply: str
    concept_summary: str
    suggested_practice_topic: str
    follow_up_prompt: str
    mode: str = "curriculum_verified_tutor"

@router.get("/diagnostic-context")
def get_tutor_diagnostic_context(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = current_user.profile
    target_role = profile.target_role if profile else "Software Developer"
    skill_level = profile.skill_level if profile else "Intermediate"
    pref_lang = profile.preferred_programming_language if profile else "Python"

    # 1. Analyze submitted answers for accuracy and weak topics
    submissions = db.query(SubmittedAnswer).filter(SubmittedAnswer.user_id == current_user.id).all()
    total_answers = len(submissions)
    correct_answers = sum(1 for s in submissions if s.is_correct)
    overall_accuracy = round((correct_answers / max(1, total_answers)) * 100, 1)

    # Group by topic
    topic_stats: Dict[str, Dict[str, int]] = {}
    for s in submissions:
        t_name = s.question.topic.name if (s.question and s.question.topic) else "General Aptitude"
        if t_name not in topic_stats:
            topic_stats[t_name] = {"total": 0, "correct": 0}
        topic_stats[t_name]["total"] += 1
        if s.is_correct:
            topic_stats[t_name]["correct"] += 1

    weak_topics = []
    for t_name, stats in topic_stats.items():
        acc = (stats["correct"] / stats["total"]) * 100
        if acc < 65.0 or stats["total"] - stats["correct"] >= 2:
            weak_topics.append({"topic": t_name, "accuracy": round(acc, 1), "failed": stats["total"] - stats["correct"]})

    weak_topics.sort(key=lambda x: x["accuracy"])
    primary_weak_topic = weak_topics[0]["topic"] if weak_topics else "Dynamic Programming & Trees"

    # 2. Coding problem stats
    coding_subs = db.query(CodingSubmission).filter(CodingSubmission.user_id == current_user.id).all()
    coding_solved = sum(1 for c in coding_subs if c.status == "accepted")

    # 3. Communication stats
    comm_sessions = db.query(CommunicationSession).filter(CommunicationSession.user_id == current_user.id).all()
    avg_comm_score = round(sum(cs.overall_score for cs in comm_sessions) / max(1, len(comm_sessions)), 1) if comm_sessions else 7.5

    return {
        "student_name": current_user.full_name or "Candidate",
        "target_role": target_role,
        "skill_level": skill_level,
        "primary_language": pref_lang,
        "mcq_questions_attempted": total_answers,
        "mcq_accuracy_percentage": overall_accuracy,
        "weak_topics": [w["topic"] for w in weak_topics[:3]],
        "primary_weak_topic": primary_weak_topic,
        "coding_problems_solved": coding_solved,
        "communication_average_score": avg_comm_score,
        "recommended_next_step": f"Deep-dive into {primary_weak_topic} followed by 5 practice assessments."
    }

@router.post("/chat", response_model=TutorChatResponse)
def tutor_chat(
    payload: TutorChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    msg = payload.message.strip().lower()
    profile = current_user.profile
    target_role = profile.target_role if profile else "Software Developer"
    pref_lang = profile.preferred_programming_language if profile else "Python"

    # Knowledge bases for common placement engineering domains
    if any(k in msg for k in ["dp", "dynamic programming", "memoization", "tabulation"]):
        reply = (
            f"Dynamic Programming is simply **recursion without repeating identical subproblems**. "
            f"For your target role as a {target_role}, interviewers test two core approaches:\n\n"
            f"1. **Top-Down (Memoization)**: Write standard recursion, then cache the result of each state in a dictionary/array before returning.\n"
            f"2. **Bottom-Up (Tabulation)**: Initialize a base-case array `dp = [0]*(n+1)` and iteratively solve from smallest subproblems to target `n`.\n\n"
            f"**Golden Rule**: If a problem exhibits overlapping subproblems and optimal substructure, define your DP state clearly: `dp[i]` = optimal answer for size `i`."
        )
        concept = "Dynamic Programming: Overlapping Subproblems & State Transitions"
        suggested = "Dynamic Programming & Trees"
        follow_up = "Would you like me to walk through the 0/1 Knapsack recurrence relation or the Coin Change state transition?"

    elif any(k in msg for k in ["sql", "database", "index", "b-tree", "acid"]):
        reply = (
            f"In database systems, an **Index** acts like an alphabetical index at the back of a textbook. "
            f"Without an index, the database engine must execute a **Full Table Scan ($O(N)$)** inspecting every single row on disk.\n\n"
            f"**B-Tree Indexes ($O(\\log N)$)**:\n"
            f"- Balanced search trees where leaf nodes store data pointers or clustered row tuples.\n"
            f"- Enables range queries (`BETWEEN`, `>`, `<`) and exact lookups efficiently.\n\n"
            f"**Interview Trap**: Don't index every column! Writes (`INSERT`, `UPDATE`, `DELETE`) become slower because the B-Tree must be balanced and written on every mutation."
        )
        concept = "Database Indexing & B-Tree Storage Architecture"
        suggested = "DBMS & SQL"
        follow_up = "Do you want to compare Clustered vs Non-Clustered Indexes, or analyze how Composite Indexes require the leftmost prefix rule?"

    elif any(k in msg for k in ["weak", "diagnose", "practice", "recommend", "where should i start"]):
        reply = (
            f"Based on your placement preparation trajectory for **{target_role}**:\n\n"
            f"- **Core Technical Priority**: Master algorithmic problem decomposition and edge-case testing in {pref_lang}.\n"
            f"- **Assessment Focus**: Quantitative speed (time-work & speed-distance) and SQL multi-table JOINs.\n"
            f"- **Recommended Exercise**: Complete 1 daily challenge sprint and simulate one 45-minute company round."
        )
        concept = "Diagnostic Profile Calibration"
        suggested = "Quantitative Aptitude & Placement Papers"
        follow_up = "Shall we solve a sample interview problem on Time & Work, or a coding challenge on Sliding Windows?"

    elif any(k in msg for k in ["resume", "project", "interview", "hr", "star"]):
        reply = (
            f"For tech resumes and project defense rounds, apply the **XYZ Formula** (Google standard):\n"
            f"*'Accomplished [X] as measured by [Y], by doing [Z]'*.\n\n"
            f"Instead of writing: *'Built a web application for booking'*\n"
            f"Write: *'Engineered full-stack booking system with FastAPI and React, supporting 50 concurrent transactions with sub-80ms API response latency using Redis caching.'*\n\n"
            f"During HR behavioral rounds, always frame your answers using **STAR**: Situation $\\to$ Task $\\to$ Action $\\to$ Result."
        )
        concept = "Resume Project Defense & STAR Behavioral Rubric"
        suggested = "HR Interview Preparation"
        follow_up = "Tell me about one project you built, and I will help you formulate the exact architectural defense script for recruiters."

    else:
        reply = (
            f"Hello! I am your **InterviewAI Placement Tutor**. As you prepare for {target_role} roles, "
            f"I help calibrate your conceptual depth in Data Structures, Core CS (OS/DBMS/Networks), "
            f"Coding challenges in {pref_lang}, and behavioral interview defense.\n\n"
            f"You can ask me to explain any difficult technical concept, diagnose your weak areas, or walk through algorithmic trade-offs step-by-step."
        )
        concept = "General Placement Advisory & Algorithmic Tutoring"
        suggested = "Data Structures & Core CS"
        follow_up = "What technical concept or interview round would you like to master today?"

    return TutorChatResponse(
        reply=reply,
        concept_summary=concept,
        suggested_practice_topic=suggested,
        follow_up_prompt=follow_up,
        mode="curriculum_verified_tutor"
    )

