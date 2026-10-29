from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from app.core.database import get_db
from app.models.models import User, Topic, Question, SubmittedAnswer
from app.schemas.schemas import DashboardStats
from app.api.deps import get_current_user
from app.services.dashboard_service import dashboard_service

router = APIRouter(prefix="/progress", tags=["Progress & Diagnostics"])
dashboard_router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary", response_model=DashboardStats)
@router.get("/stats", response_model=DashboardStats)
@dashboard_router.get("/stats", response_model=DashboardStats)
def get_progress_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return dashboard_service.get_student_stats(db, current_user)

@router.get("/topics")
def get_topic_progress(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    topic_perf = db.query(
        Topic.name,
        Topic.category,
        func.count(SubmittedAnswer.id).label("total"),
        func.sum(case((SubmittedAnswer.is_correct == True, 1), else_=0)).label("correct")
    ).join(Question, Question.topic_id == Topic.id)\
     .join(SubmittedAnswer, SubmittedAnswer.question_id == Question.id)\
     .filter(SubmittedAnswer.user_id == current_user.id)\
     .group_by(Topic.id).all()

    out = []
    for name, category, total, correct in topic_perf:
        tot = total or 0
        corr = correct or 0
        pct = round((corr / tot * 100), 1) if tot > 0 else 0.0
        out.append({
            "topic": name,
            "category": category,
            "total_attempts": tot,
            "correct_attempts": corr,
            "accuracy_percentage": pct
        })
    return out

