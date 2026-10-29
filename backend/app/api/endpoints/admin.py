from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from app.core.database import get_db
from app.models.models import (
    User, Question, QuestionOption, Topic, Lesson, LearningResource,
    PracticeSession, SubmittedAnswer, CodingProblem, InterviewSession, Subject, utc_now
)
from app.api.deps import get_current_admin

router = APIRouter(prefix="/admin", tags=["Administrator Management"])

class QuestionCreateReq(BaseModel):
    topic_id: int
    question_type: str = "aptitude_mcq"
    difficulty: str = "intermediate"
    question_text: str
    code_snippet: Optional[str] = None
    explanation: str
    step_by_step_reasoning: str
    practical_example: str
    common_mistake: str
    learning_tip: str
    related_concept_url: Optional[str] = None
    options: List[Dict[str, Any]]

class TopicCreateReq(BaseModel):
    name: str
    slug: str
    category: str
    subcategory: str
    description: str
    icon: str = "BookOpen"

class LessonCreateReq(BaseModel):
    topic_id: int
    title: str
    slug: str
    difficulty: str = "Beginner"
    content_markdown: str
    key_takeaways: List[str]
    estimated_minutes: int = 15
    order_index: int = 1

class ResourceCreateReq(BaseModel):
    topic_id: int
    title: str
    url: str
    resource_type: str = "documentation"
    provider_name: str
    language: str = "English"
    description: str

@router.get("/analytics")
def get_platform_analytics(
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    total_users = db.query(User).count()
    total_students = db.query(User).filter(User.role == "student").count()
    total_sessions = db.query(PracticeSession).count()
    total_answers = db.query(SubmittedAnswer).count()
    correct_answers = db.query(SubmittedAnswer).filter(SubmittedAnswer.is_correct == True).count()
    avg_accuracy = round((correct_answers / total_answers * 100), 1) if total_answers > 0 else 0.0

    total_questions = db.query(Question).count()
    total_coding = db.query(CodingProblem).count()
    total_interviews = db.query(InterviewSession).count()

    category_distribution = db.query(
        Topic.category,
        func.count(Question.id)
    ).join(Question, Question.topic_id == Topic.id).group_by(Topic.category).all()

    return {
        "total_users": total_users,
        "total_students": total_students,
        "total_sessions": total_sessions,
        "total_answers_submitted": total_answers,
        "average_platform_accuracy": avg_accuracy,
        "total_questions_in_bank": total_questions,
        "total_coding_problems": total_coding,
        "total_mock_interviews": total_interviews,
        "question_category_distribution": [
            {"category": cat, "count": cnt} for cat, cnt in category_distribution
        ]
    }

@router.get("/users")
def list_users(
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    users = db.query(User).order_by(User.created_at.desc()).all()
    return [
        {
            "id": u.id,
            "email": u.email,
            "full_name": u.full_name,
            "role": u.role,
            "is_active": u.is_active,
            "last_login_at": u.last_login_at.strftime("%Y-%m-%d %H:%M") if u.last_login_at else None,
            "created_at": u.created_at.strftime("%Y-%m-%d %H:%M")
        } for u in users
    ]

@router.post("/users/{user_id}/toggle-status")
def toggle_user_status(
    user_id: int,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    if user_id == admin.id:
        raise HTTPException(status_code=400, detail="Cannot deactivate your own administrator account.")
    u = db.query(User).filter(User.id == user_id).first()
    if not u:
        raise HTTPException(status_code=404, detail="User not found.")
    u.is_active = not u.is_active
    db.commit()
    return {"message": f"User status set to {'active' if u.is_active else 'inactive'}.", "is_active": u.is_active}

@router.get("/questions")
def list_admin_questions(
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    questions = db.query(Question).order_by(Question.id.desc()).all()
    out = []
    for q in questions:
        out.append({
            "id": q.id,
            "topic_id": q.topic_id,
            "topic_name": q.topic.name if q.topic else "General",
            "category": q.topic.category if q.topic else "General",
            "question_type": q.question_type,
            "difficulty": q.difficulty,
            "question_text": q.question_text,
            "is_published": q.is_published,
            "options": [
                {
                    "option_key": opt.option_key,
                    "option_text": opt.option_text,
                    "is_correct": opt.is_correct,
                    "why_wrong_explanation": opt.why_wrong_explanation
                } for opt in q.options
            ],
            "explanation": q.explanation
        })
    return out

@router.post("/questions")
def create_question(
    payload: QuestionCreateReq,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    q = Question(
        topic_id=payload.topic_id,
        question_type=payload.question_type,
        difficulty=payload.difficulty,
        question_text=payload.question_text,
        code_snippet=payload.code_snippet,
        explanation=payload.explanation,
        step_by_step_reasoning=payload.step_by_step_reasoning,
        practical_example=payload.practical_example,
        common_mistake=payload.common_mistake,
        learning_tip=payload.learning_tip,
        related_concept_url=payload.related_concept_url,
        is_published=True,
        created_at=utc_now()
    )
    db.add(q)
    db.flush()

    for opt_data in payload.options:
        opt = QuestionOption(
            question_id=q.id,
            option_key=opt_data["option_key"],
            option_text=opt_data["option_text"],
            is_correct=opt_data.get("is_correct", False),
            why_wrong_explanation=opt_data.get("why_wrong_explanation", "")
        )
        db.add(opt)

    db.commit()
    return {"message": "Question created successfully.", "question_id": q.id}

@router.delete("/questions/{question_id}")
def delete_question(
    question_id: int,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    q = db.query(Question).filter(Question.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found.")
    db.delete(q)
    db.commit()
    return {"message": "Question deleted successfully."}

@router.post("/topics")
def create_topic(
    payload: TopicCreateReq,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    existing = db.query(Topic).filter(Topic.slug == payload.slug).first()
    if existing:
        raise HTTPException(status_code=400, detail="Topic slug already exists.")
    t = Topic(
        name=payload.name,
        slug=payload.slug,
        category=payload.category,
        subcategory=payload.subcategory,
        description=payload.description,
        icon=payload.icon
    )
    db.add(t)
    db.commit()
    return {"message": "Topic created successfully.", "topic_id": t.id}

@router.post("/lessons")
def create_lesson(
    payload: LessonCreateReq,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    l = Lesson(
        topic_id=payload.topic_id,
        title=payload.title,
        slug=payload.slug,
        difficulty=payload.difficulty,
        content_markdown=payload.content_markdown,
        key_takeaways=payload.key_takeaways,
        estimated_minutes=payload.estimated_minutes,
        order_index=payload.order_index,
        is_published=True
    )
    db.add(l)
    db.commit()
    return {"message": "Lesson created successfully.", "lesson_id": l.id}

@router.post("/resources")
def create_resource(
    payload: ResourceCreateReq,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    r = LearningResource(
        topic_id=payload.topic_id,
        title=payload.title,
        url=payload.url,
        resource_type=payload.resource_type,
        provider_name=payload.provider_name,
        language=payload.language,
        description=payload.description,
        is_verified=True
    )
    db.add(r)
    db.commit()
    return {"message": "Resource created successfully.", "resource_id": r.id}
