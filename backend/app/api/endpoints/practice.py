from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from app.core.database import get_db
from app.models.models import User, Question, Topic, PracticeSession, SessionQuestion
from app.schemas.schemas import (
    PracticeSessionCreate, PracticeSessionDetail, SubmitAnswerRequest,
    AnswerFeedback, QuestionPublic, QuestionOptionPublic
)
from app.api.deps import get_current_user
from app.services.practice_service import practice_service

router = APIRouter(prefix="/practice", tags=["Practice & Assessment"])

class SubmitAnswerBody(BaseModel):
    question_id: int
    selected_option: Optional[str] = None
    submitted_answer: Optional[str] = None

@router.post("/sessions", response_model=PracticeSessionDetail)
@router.post("/session", response_model=PracticeSessionDetail)
def start_practice_session(
    payload: PracticeSessionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session = practice_service.create_session(
        db=db,
        user_id=current_user.id,
        category=payload.category,
        subcategory=payload.subcategory,
        difficulty=payload.difficulty or "all",
        question_count=payload.question_count,
        session_mode=payload.session_mode or "practice",
        time_limit_seconds=payload.time_limit_seconds
    )
    return practice_service.get_session_detail(db, session.id, current_user.id)

class MarkReviewBody(BaseModel):
    question_index: int
    is_marked: bool

@router.post("/sessions/{session_id}/mark-review")
def mark_question_for_review(
    session_id: int,
    payload: MarkReviewBody,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    marks = practice_service.toggle_mark_for_review(
        db=db,
        user_id=current_user.id,
        session_id=session_id,
        question_index=payload.question_index,
        is_marked=payload.is_marked
    )
    return {"session_id": session_id, "marked_indices": marks}

@router.post("/sessions/{session_id}/complete", response_model=PracticeSessionDetail)
def complete_practice_session(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return practice_service.complete_session(db, current_user.id, session_id)

@router.get("/sessions/{session_id}", response_model=PracticeSessionDetail)
@router.get("/session/{session_id}", response_model=PracticeSessionDetail)
def get_session(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return practice_service.get_session_detail(db, session_id, current_user.id)

@router.get("/sessions/{session_id}/questions")
def get_session_questions(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session_detail = practice_service.get_session_detail(db, session_id, current_user.id)
    return session_detail.questions

@router.post("/sessions/{session_id}/answers", response_model=AnswerFeedback)
@router.post("/sessions/{session_id}/submit", response_model=AnswerFeedback)
def submit_session_answer(
    session_id: int,
    payload: SubmitAnswerBody,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    ans = payload.selected_option or payload.submitted_answer or "A"
    return practice_service.submit_answer(
        db=db,
        user_id=current_user.id,
        question_id=payload.question_id,
        selected_option=ans,
        session_id=session_id
    )

@router.post("/submit", response_model=AnswerFeedback)
def submit_answer_legacy(
    payload: SubmitAnswerRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return practice_service.submit_answer(
        db=db,
        user_id=current_user.id,
        question_id=payload.question_id,
        selected_option=payload.selected_option,
        session_id=payload.session_id
    )

@router.post("/sessions/{session_id}/next")
def next_session_question(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session = practice_service.get_session_detail(db, session_id, current_user.id)
    next_q = next((q for q in session.questions if not q.is_answered), None)
    return {
        "has_next": next_q is not None,
        "next_question": next_q,
        "is_completed": session.status == "completed" or next_q is None
    }

@router.get("/sessions/{session_id}/summary")
def get_session_summary(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session = practice_service.get_session_detail(db, session_id, current_user.id)
    incorrect_count = max(0, session.completed_questions - session.correct_count)
    return {
        "session_id": session.id,
        "category": session.category,
        "subcategory": session.subcategory,
        "total_questions": session.total_questions,
        "completed_questions": session.completed_questions,
        "correct_count": session.correct_count,
        "incorrect_count": incorrect_count,
        "score_percentage": session.score_percentage,
        "accuracy": session.score_percentage,
        "status": session.status,
        "questions_breakdown": [
            {
                "order_index": q.order_index,
                "is_correct": q.is_correct,
                "submitted_answer": q.submitted_answer,
                "question_text": q.question.question_text
            }
            for q in session.questions
        ]
    }

@router.get("/questions", response_model=List[QuestionPublic])
def list_questions(
    limit: int = Query(50, ge=1, le=500),
    skip: int = Query(0, ge=0),
    category: Optional[str] = None,
    difficulty: Optional[str] = None,
    topic_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Question).filter(Question.is_published == True)
    if topic_id:
        query = query.filter(Question.topic_id == topic_id)
    if difficulty and difficulty != "all":
        query = query.filter(Question.difficulty == difficulty)
    if category:
        query = query.join(Topic).filter(Topic.category == category)
    return query.offset(skip).limit(limit).all()

@router.get("/daily-challenge")
def get_daily_challenge(db: Session = Depends(get_db)):
    from datetime import datetime
    from app.models.models import CodingProblem, QuestionOption
    day = datetime.now().timetuple().tm_yday

    apt_q = db.query(Question).join(Topic).filter(
        Topic.category.in_(["quantitative", "logical", "verbal"]),
        Question.is_published == True
    ).offset(day % max(1, db.query(Question).count())).first()

    if not apt_q:
        apt_q = db.query(Question).first()

    code_prob = db.query(CodingProblem).offset(day % max(1, db.query(CodingProblem).count())).first()

    tech_q = db.query(Question).join(Topic).filter(
        Topic.category == "technical",
        Question.is_published == True
    ).offset((day + 5) % max(1, db.query(Question).count())).first()
    if not tech_q:
        tech_q = apt_q

    hr_questions = [
        "Tell me about a time you handled a tight project deadline under unexpected pressure.",
        "Why should our company hire you over other qualified college graduates?",
        "Describe a complex technical conflict you had with a teammate and how you resolved it.",
        "What are your greatest technical strengths and what is one area you are actively improving?",
        "Where do you see yourself in 3 years, and what technical milestones do you plan to achieve?"
    ]
    daily_hr = hr_questions[day % len(hr_questions)]

    def serialize_q(q):
        if not q:
            return None
        correct_opt = next((opt.option_key for opt in q.options if opt.is_correct), "A")
        return {
            "id": q.id,
            "question_text": q.question_text,
            "difficulty": q.difficulty,
            "topic_name": q.topic.name if q.topic else "General",
            "options": [{"key": opt.option_key, "text": opt.option_text} for opt in q.options],
            "correct_option": correct_opt,
            "explanation": q.explanation,
            "step_by_step_reasoning": q.step_by_step_reasoning,
            "common_mistake": q.common_mistake,
            "concept": q.topic.name if q.topic else "General"
        }

    return {
        "date": datetime.now().strftime("%B %d, %Y"),
        "aptitude_problem": serialize_q(apt_q),
        "technical_problem": serialize_q(tech_q),
        "coding_problem": {
            "id": code_prob.id if code_prob else 1,
            "title": code_prob.title if code_prob else "Two Sum",
            "difficulty": code_prob.difficulty if code_prob else "Easy",
            "category": code_prob.category if code_prob else "Arrays",
            "description": code_prob.description if code_prob else "Find two numbers in array that add up to target.",
            "starter_code": (code_prob.starter_code_python or code_prob.starter_code_cpp) if code_prob else "def solution():\n    pass"
        } if code_prob else None,
        "hr_question": daily_hr
    }

@router.get("/revision")
def get_revision_centre(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.models.models import SubmittedAnswer
    submissions = db.query(SubmittedAnswer).filter(
        SubmittedAnswer.user_id == current_user.id
    ).order_by(SubmittedAnswer.created_at.desc()).limit(100).all()

    out = []
    for s in submissions:
        q = s.question
        if not q:
            continue
        correct_opt = next((opt.option_key for opt in q.options if opt.is_correct), "A")
        out.append({
            "id": s.id,
            "question_id": q.id,
            "question_text": q.question_text,
            "topic": q.topic.name if q.topic else "General",
            "difficulty": q.difficulty,
            "selected_option": s.selected_option,
            "correct_option": correct_opt,
            "is_correct": s.is_correct,
            "explanation": q.explanation,
            "step_by_step_reasoning": q.step_by_step_reasoning,
            "misconception": q.common_mistake or "Review the fundamental formula.",
            "attempted_at": s.created_at.strftime("%b %d, %Y - %I:%M %p")
        })
    return out
