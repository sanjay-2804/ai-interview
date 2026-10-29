from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import User, UserProfile, utc_now
from app.schemas.schemas import UserProfileOut, ProfileUpdate
from app.api.deps import get_current_user

router = APIRouter(prefix="/profile", tags=["Student Profile"])

@router.get("", response_model=UserProfileOut)
@router.get("/", response_model=UserProfileOut)
def get_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = current_user.profile
    if not profile:
        profile = UserProfile(
            user_id=current_user.id,
            target_role="Software Developer",
            preferred_programming_language="Python",
            skill_level="Beginner",
            study_availability=2.5,
            preferred_topics=["Data Structures", "Aptitude"],
            prep_priorities=["Campus Placement"],
            onboarding_completed=False
        )
        db.add(profile)
        db.commit()
        db.refresh(profile)
    return UserProfileOut.model_validate(profile)

@router.patch("", response_model=UserProfileOut)
@router.patch("/", response_model=UserProfileOut)
@router.put("", response_model=UserProfileOut)
@router.put("/", response_model=UserProfileOut)
@router.post("", response_model=UserProfileOut)
@router.post("/", response_model=UserProfileOut)
def update_profile(
    payload: ProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = current_user.profile
    if not profile:
        profile = UserProfile(
            user_id=current_user.id,
            target_role="Software Developer",
            preferred_programming_language="Python",
            skill_level="Beginner",
            study_availability=2.0,
            preferred_topics=["Data Structures", "Aptitude"],
            prep_priorities=["Campus Placement"],
            onboarding_completed=False
        )
        db.add(profile)

    if payload.college is not None:
        profile.college = payload.college
    if payload.course is not None:
        profile.course = payload.course
    if payload.study_year is not None:
        profile.study_year = payload.study_year
    if payload.target_role is not None:
        profile.target_role = payload.target_role
    
    lang = payload.preferred_programming_language or payload.preferred_language
    if lang is not None:
        profile.preferred_programming_language = lang
    if payload.skill_level is not None:
        profile.skill_level = payload.skill_level
    if payload.study_availability is not None:
        val = payload.study_availability
        if isinstance(val, (int, float)):
            profile.study_availability = float(val)
        else:
            s = str(val).lower().strip()
            if "30 min" in s:
                profile.study_availability = 0.5
            else:
                digits = "".join(ch for ch in s.split()[0] if ch.isdigit() or ch == '.')
                try:
                    profile.study_availability = float(digits) if digits else 2.0
                except ValueError:
                    profile.study_availability = 2.0
    if payload.preferred_topics is not None:
        profile.preferred_topics = payload.preferred_topics
    if payload.prep_priorities is not None:
        profile.prep_priorities = payload.prep_priorities

    profile.onboarding_completed = True
    profile.updated_at = utc_now()

    db.commit()
    db.refresh(profile)
    return UserProfileOut.model_validate(profile)

