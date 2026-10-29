from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import User
from app.schemas.schemas import DashboardStats
from app.api.deps import get_current_user
from app.services.dashboard_service import dashboard_service

router = APIRouter(prefix="/dashboard", tags=["Student Dashboard"])

@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return dashboard_service.get_student_stats(db, current_user)

