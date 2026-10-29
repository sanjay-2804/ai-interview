from fastapi import APIRouter
from app.api.endpoints import (
    auth, profile, onboarding, learning, practice, coding,
    interviews, roadmap, resume, projects, bookmarks, admin, progress,
    communication, tutor
)

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(profile.router)
api_router.include_router(onboarding.router)
api_router.include_router(learning.router, prefix="/learning")
api_router.include_router(learning.router)
api_router.include_router(practice.router)
api_router.include_router(coding.router)
api_router.include_router(communication.router)
api_router.include_router(interviews.router)
api_router.include_router(roadmap.router)
api_router.include_router(resume.router)
api_router.include_router(projects.router)
api_router.include_router(bookmarks.router)
api_router.include_router(admin.router)
api_router.include_router(progress.router)
api_router.include_router(progress.dashboard_router)
api_router.include_router(tutor.router)
