from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.models.models import User, Topic, Lesson, LearningResource, LessonProgress, ActivityEvent, utc_now
from app.schemas.schemas import LessonDetail, TopicDetail, LearningResourceOut
from app.api.deps import get_current_user

router = APIRouter(prefix="/lessons", tags=["Technical Learning Centre"])

@router.get("/topics")
def list_topics(
    category: Optional[str] = None,
    subcategory: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Topic)
    if category:
        query = query.filter(Topic.category == category)
    if subcategory:
        query = query.filter(Topic.subcategory == subcategory)

    topics = query.all()
    out = []
    for t in topics:
        out.append({
            "id": t.id,
            "name": t.name,
            "slug": t.slug,
            "category": t.category,
            "subcategory": t.subcategory,
            "description": t.description,
            "icon": t.icon,
            "lesson_count": len(t.lessons),
            "resource_count": len(t.resources),
            "question_count": len(t.questions),
            "coding_count": len(t.coding_problems)
        })
    return out

@router.get("/topic/{slug}", response_model=TopicDetail)
def get_topic_by_slug(
    slug: str,
    db: Session = Depends(get_db)
):
    topic = db.query(Topic).filter(Topic.slug == slug).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found.")

    lessons = [
        {
            "id": l.id,
            "title": l.title,
            "slug": l.slug,
            "difficulty": l.difficulty,
            "estimated_minutes": l.estimated_minutes,
            "order_index": l.order_index
        }
        for l in sorted(topic.lessons, key=lambda x: x.order_index)
    ]

    resources = [LearningResourceOut.model_validate(r) for r in topic.resources]

    return TopicDetail(
        id=topic.id,
        name=topic.name,
        slug=topic.slug,
        category=topic.category,
        subcategory=topic.subcategory,
        description=topic.description,
        icon=topic.icon,
        lessons=lessons,
        resources=resources,
        question_count=len(topic.questions),
        coding_count=len(topic.coding_problems)
    )

@router.get("/lesson/{lesson_id}", response_model=LessonDetail)
def get_lesson(
    lesson_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found.")

    progress = db.query(LessonProgress).filter(
        LessonProgress.user_id == current_user.id,
        LessonProgress.lesson_id == lesson_id
    ).first()

    resources = [LearningResourceOut.model_validate(r) for r in lesson.topic.resources]

    return LessonDetail(
        id=lesson.id,
        topic_id=lesson.topic_id,
        title=lesson.title,
        slug=lesson.slug,
        difficulty=lesson.difficulty,
        content_markdown=lesson.content_markdown,
        key_takeaways=lesson.key_takeaways,
        estimated_minutes=lesson.estimated_minutes,
        is_completed=bool(progress and progress.status == "completed"),
        resources=resources
    )

@router.post("/lesson/{lesson_id}/complete")
def complete_lesson(
    lesson_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found.")

    progress = db.query(LessonProgress).filter(
        LessonProgress.user_id == current_user.id,
        LessonProgress.lesson_id == lesson_id
    ).first()

    if not progress:
        progress = LessonProgress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            status="completed",
            completed_at=utc_now()
        )
        db.add(progress)

        activity = ActivityEvent(
            user_id=current_user.id,
            event_type="lesson_complete",
            title=f"Completed lesson: {lesson.title}",
            details=f"Topic: {lesson.topic.name}",
            metadata_json={"lesson_id": lesson.id}
        )
        db.add(activity)
        db.commit()

    return {"message": "Lesson marked as completed.", "lesson_id": lesson_id}

