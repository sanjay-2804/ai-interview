from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.models import User, InterviewSession
from app.schemas.schemas import (
    MockInterviewStart, MockInterviewSubmitAnswer, MockInterviewDetail
)
from app.api.deps import get_current_user
from app.services.interview_service import interview_service

router = APIRouter(prefix="/interview", tags=["Mock Interview Centre"])

@router.post("/start", response_model=MockInterviewDetail)
def start_interview(
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

@router.get("/{session_id}", response_model=MockInterviewDetail)
def get_interview(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return interview_service.get_interview(db, session_id, current_user.id)

@router.post("/submit-response", response_model=MockInterviewDetail)
async def submit_response(
    payload: MockInterviewSubmitAnswer,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return await interview_service.submit_response(
        db=db,
        session_id=payload.session_id,
        user_id=current_user.id,
        response_text=payload.response_text
    )

@router.get("/history/list")
def get_interview_history(
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

