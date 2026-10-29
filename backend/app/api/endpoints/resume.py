from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import User, Resume, ActivityEvent, utc_now
from app.schemas.schemas import ResumeOut, ResumeUpdate
from app.api.deps import get_current_user
from app.services.ai_service import ai_service

router = APIRouter(prefix="/resume", tags=["Resume & Projects"])

@router.get("/my-resume", response_model=ResumeOut)
def get_my_resume(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    resume = current_user.resume
    if not resume:
        resume = Resume(
            user_id=current_user.id,
            title="Placement Resume",
            full_name=current_user.full_name,
            email=current_user.email,
            education_json=[],
            skills_json=[],
            projects_json=[],
            experience_json=[],
            certifications_json=[],
            links_json={}
        )
        db.add(resume)
        db.commit()
        db.refresh(resume)
    return ResumeOut.model_validate(resume)

@router.put("/my-resume", response_model=ResumeOut)
def update_my_resume(
    payload: ResumeUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    resume = current_user.resume
    if not resume:
        resume = Resume(user_id=current_user.id)
        db.add(resume)

    resume.title = payload.title or resume.title
    resume.full_name = payload.full_name
    resume.email = payload.email
    resume.phone = payload.phone
    resume.location = payload.location
    resume.target_role = payload.target_role
    resume.summary = payload.summary
    resume.education_json = payload.education_json
    resume.skills_json = payload.skills_json
    resume.projects_json = payload.projects_json
    resume.experience_json = payload.experience_json
    resume.certifications_json = payload.certifications_json
    resume.links_json = payload.links_json
    resume.updated_at = utc_now()

    db.commit()
    db.refresh(resume)
    return ResumeOut.model_validate(resume)

@router.post("/review")
async def review_resume(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    resume = current_user.resume
    if not resume:
        raise HTTPException(status_code=404, detail="No resume found to review.")

    resume_dict = {
        "full_name": resume.full_name,
        "summary": resume.summary,
        "skills_json": resume.skills_json,
        "projects_json": resume.projects_json,
        "education_json": resume.education_json,
        "experience_json": resume.experience_json
    }

    feedback = await ai_service.review_resume(resume_dict)
    resume.ai_review_feedback = feedback
    db.commit()

    return feedback

