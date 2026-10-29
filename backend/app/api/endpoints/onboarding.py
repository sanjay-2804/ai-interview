from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import User, UserProfile, utc_now
from app.schemas.schemas import OnboardingUpdate, UserProfileOut
from app.api.deps import get_current_user

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])

@router.post("", response_model=UserProfileOut)
@router.post("/", response_model=UserProfileOut)
@router.patch("", response_model=UserProfileOut)
@router.patch("/", response_model=UserProfileOut)
@router.put("", response_model=UserProfileOut)
@router.put("/", response_model=UserProfileOut)
def update_onboarding(
    payload: OnboardingUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = current_user.profile
    if not profile:
        profile = UserProfile(user_id=current_user.id)
        db.add(profile)

    if payload.college is not None:
        profile.college = payload.college

    course_val = payload.course if payload.course is not None else payload.degree
    if course_val is not None:
        profile.course = course_val

    year_val = payload.study_year if payload.study_year is not None else payload.graduation_year
    if year_val is not None:
        profile.study_year = year_val

    if payload.target_role is not None:
        profile.target_role = payload.target_role

    lang_val = payload.preferred_programming_language if payload.preferred_programming_language is not None else payload.preferred_language
    if lang_val is not None:
        profile.preferred_programming_language = lang_val

    if payload.skill_level is not None:
        profile.skill_level = payload.skill_level

    avail_val = payload.study_availability if payload.study_availability is not None else payload.study_hours_per_day
    if avail_val is not None:
        profile.study_availability = avail_val

    if payload.preferred_topics is not None:
        profile.preferred_topics = payload.preferred_topics

    if payload.prep_priorities is not None:
        profile.prep_priorities = payload.prep_priorities

    profile.onboarding_completed = True
    profile.updated_at = utc_now()

    db.commit()
    db.refresh(profile)
    return UserProfileOut.model_validate(profile)
