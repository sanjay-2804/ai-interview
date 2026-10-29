from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone

# --- Auth & User Schemas ---

class UserRegister(BaseModel):
    full_name: Optional[str] = None
    name: Optional[str] = None
    email: EmailStr
    password: str = Field(..., min_length=6)
    confirm_password: Optional[str] = None
    target_role: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def resolve_name(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if not data.get("full_name") and data.get("name"):
                data["full_name"] = data["name"]
        return data

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    remember_me: Optional[bool] = False

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ForgotPasswordResponse(BaseModel):
    message: str
    reset_token: Optional[str] = None  # Returned for local testing when email delivery is not configured

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(..., min_length=6)

class UserProfileOut(BaseModel):
    id: int
    college: Optional[str] = None
    course: Optional[str] = None
    degree: Optional[str] = None
    study_year: Optional[str] = None
    graduation_year: Optional[str] = None
    target_role: str
    preferred_programming_language: str
    preferred_language: Optional[str] = None
    skill_level: str
    study_availability: float
    study_hours_per_day: Optional[float] = None
    preferred_topics: List[str] = Field(default_factory=list)
    prep_priorities: List[str] = Field(default_factory=list)
    onboarding_completed: bool = False

    @model_validator(mode="before")
    @classmethod
    def populate_aliases(cls, data: Any) -> Any:
        if hasattr(data, "__dict__") or not isinstance(data, dict):
            c = getattr(data, "course", None)
            y = getattr(data, "study_year", None)
            lang = getattr(data, "preferred_programming_language", "Python")
            avail = getattr(data, "study_availability", 2.0)
            return {
                "id": getattr(data, "id", 0),
                "college": getattr(data, "college", None),
                "course": c,
                "degree": c,
                "study_year": y,
                "graduation_year": y,
                "target_role": getattr(data, "target_role", "Software Developer"),
                "preferred_programming_language": lang,
                "preferred_language": lang,
                "skill_level": getattr(data, "skill_level", "Beginner"),
                "study_availability": avail,
                "study_hours_per_day": avail,
                "preferred_topics": getattr(data, "preferred_topics", []) or [],
                "prep_priorities": getattr(data, "prep_priorities", []) or [],
                "onboarding_completed": getattr(data, "onboarding_completed", False),
            }
        elif isinstance(data, dict):
            c = data.get("course") or data.get("degree")
            y = data.get("study_year") or data.get("graduation_year")
            lang = data.get("preferred_programming_language") or data.get("preferred_language") or "Python"
            avail = data.get("study_availability") or data.get("study_hours_per_day") or 2.0
            data["course"] = c
            data["degree"] = c
            data["study_year"] = y
            data["graduation_year"] = y
            data["preferred_programming_language"] = lang
            data["preferred_language"] = lang
            data["study_availability"] = avail
            data["study_hours_per_day"] = avail
        return data

    class Config:
        from_attributes = True

class OnboardingUpdate(BaseModel):
    college: Optional[str] = None
    course: Optional[str] = None
    degree: Optional[str] = None
    study_year: Optional[str] = None
    graduation_year: Optional[str] = None
    target_role: Optional[str] = "Software Developer"
    preferred_programming_language: Optional[str] = None
    preferred_language: Optional[str] = None
    skill_level: Optional[str] = "Beginner"
    study_availability: Optional[Any] = None
    study_hours_per_day: Optional[Any] = None
    preferred_topics: Optional[List[str]] = None
    prep_priorities: Optional[List[str]] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    name: Optional[str] = None
    role: str
    is_active: bool
    is_verified: bool = True
    last_login_at: Optional[datetime] = None
    created_at: datetime
    profile: Optional[UserProfileOut] = None
    target_role: Optional[str] = None
    skill_level: Optional[str] = None
    preferred_language: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def populate_user_profile_fields(cls, data: Any) -> Any:
        if hasattr(data, "__dict__"):
            prof = getattr(data, "profile", None)
            fn = getattr(data, "full_name", "")
            return {
                "id": getattr(data, "id", 0),
                "email": getattr(data, "email", ""),
                "full_name": fn,
                "name": fn,
                "role": getattr(data, "role", "student"),
                "is_active": getattr(data, "is_active", True),
                "is_verified": getattr(data, "is_verified", True),
                "last_login_at": getattr(data, "last_login_at", None),
                "created_at": getattr(data, "created_at", datetime.now(timezone.utc)),
                "profile": prof,
                "target_role": getattr(prof, "target_role", None) if prof else None,
                "skill_level": getattr(prof, "skill_level", None) if prof else None,
                "preferred_language": getattr(prof, "preferred_programming_language", None) if prof else None
            }
        elif isinstance(data, dict):
            prof = data.get("profile") or {}
            fn = data.get("full_name") or data.get("name") or ""
            data["full_name"] = fn
            data["name"] = fn
            if isinstance(prof, dict):
                data["target_role"] = data.get("target_role") or prof.get("target_role")
                data["skill_level"] = data.get("skill_level") or prof.get("skill_level")
                data["preferred_language"] = data.get("preferred_language") or prof.get("preferred_programming_language") or prof.get("preferred_language")
            elif hasattr(prof, "target_role"):
                data["target_role"] = getattr(prof, "target_role", None)
                data["skill_level"] = getattr(prof, "skill_level", None)
                data["preferred_language"] = getattr(prof, "preferred_programming_language", None)
        return data

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut

class ProfileUpdate(BaseModel):
    college: Optional[str] = None
    course: Optional[str] = None
    study_year: Optional[str] = None
    target_role: Optional[str] = None
    preferred_programming_language: Optional[str] = None
    preferred_language: Optional[str] = None
    skill_level: Optional[str] = None
    study_availability: Optional[Any] = None
    preferred_topics: Optional[List[str]] = None
    prep_priorities: Optional[List[str]] = None
    preferences: Optional[Any] = None

# --- Subject & Topic Schemas ---

class SubjectOut(BaseModel):
    id: int
    name: str
    slug: str
    description: str
    icon: str

    class Config:
        from_attributes = True

# --- Question & Practice Schemas ---

class QuestionOptionPublic(BaseModel):
    option_key: str
    option_text: str

    class Config:
        from_attributes = True

class QuestionPublic(BaseModel):
    id: int
    topic_id: int
    question_type: str
    difficulty: str
    question_text: str
    code_snippet: Optional[str] = None
    options: List[QuestionOptionPublic]

    class Config:
        from_attributes = True

class OptionFeedback(BaseModel):
    option_key: str
    option_text: str
    is_correct: bool
    why_wrong: Optional[str] = None

class AnswerFeedback(BaseModel):
    question_id: int
    selected_option: str
    correct_option: str
    is_correct: bool
    status: str
    explanation: str
    step_by_step_reasoning: str
    practical_example: str
    common_mistake: str
    learning_tip: str
    related_concept_url: Optional[str] = None
    encouraging_feedback: str
    options_breakdown: List[OptionFeedback]

class SubmitAnswerRequest(BaseModel):
    session_id: Optional[int] = None
    question_id: int
    selected_option: str

class PracticeSessionCreate(BaseModel):
    category: str
    subcategory: Optional[str] = None
    difficulty: Optional[str] = "all"
    question_count: int = 5
    session_mode: Optional[str] = "practice"  # practice, timed, mock_placement, daily_challenge, weak_topic
    time_limit_seconds: Optional[int] = None

class MarkForReviewRequest(BaseModel):
    session_id: int
    question_index: int
    is_marked: bool

class SessionQuestionItem(BaseModel):
    order_index: int
    question: QuestionPublic
    is_answered: bool
    submitted_answer: Optional[str] = None
    is_correct: Optional[bool] = None
    feedback: Optional[AnswerFeedback] = None

class PracticeSessionDetail(BaseModel):
    id: int
    category: str
    subcategory: Optional[str] = None
    difficulty: str
    session_mode: Optional[str] = "practice"
    time_limit_seconds: Optional[int] = None
    marked_for_review_json: Optional[List[int]] = []
    total_questions: int
    completed_questions: int
    correct_count: int
    score_percentage: float
    status: str
    questions: List[SessionQuestionItem]

# --- Communication Lab Schemas ---

class CommunicationSubmitRequest(BaseModel):
    category: str = "Self Introduction"
    prompt_title: str
    prompt_question: str
    framework: Optional[str] = None
    transcript: str
    audio_duration_seconds: Optional[float] = 0.0
    audio_filename: Optional[str] = None

class CommunicationSessionOut(BaseModel):
    id: int
    category: str
    prompt_title: str
    prompt_question: str
    framework: Optional[str] = None
    audio_filename: Optional[str] = None
    audio_duration_seconds: float = 0.0
    transcript: str
    overall_score: float
    relevance_score: float
    clarity_score: float
    grammar_score: float
    conciseness_score: float
    delivery_score: float
    wpm: int
    filler_words_count: int
    filler_words_list: List[str] = []
    strengths: List[str] = []
    improvements: List[str] = []
    concepts_demonstrated: List[str] = []
    concepts_missing: List[str] = []
    follow_up_question: Optional[str] = None
    personalized_coaching: Optional[str] = None
    sample_answer: Optional[str] = None
    status: str = "completed"
    created_at: datetime

    class Config:
        from_attributes = True

# --- Coding Practice Schemas ---

class CodingProblemListOut(BaseModel):
    id: int
    title: str
    slug: str
    difficulty: str
    category: str
    time_complexity: str
    space_complexity: str
    external_url: Optional[str] = None
    external_platform: Optional[str] = None
    has_attempted: bool = False
    is_solved: bool = False

    class Config:
        from_attributes = True

class CodingProblemDetail(BaseModel):
    id: int
    topic_id: int
    title: str
    slug: str
    difficulty: str
    category: str
    description: str
    input_format: str
    output_format: str
    constraints: str
    sample_input: str
    sample_output: str
    starter_code_python: str
    starter_code_javascript: str
    starter_code_java: str
    starter_code_cpp: str
    solution_explanation: str
    time_complexity: str
    space_complexity: str
    hints: List[str]
    external_url: Optional[str] = None
    external_platform: Optional[str] = None

    class Config:
        from_attributes = True

class CodeRunRequest(BaseModel):
    problem_id: int
    language: str
    code: str

class CodeRunResult(BaseModel):
    status: str
    output_log: str
    runtime_ms: int
    memory_kb: int
    passed_tests: int
    total_tests: int
    is_sample_preview: bool = True
    guidance: str

# --- Mock Interview Schemas ---

class MockInterviewStart(BaseModel):
    category: str = "Technical"
    target_role: str = "Software Developer"
    difficulty: str = "Medium"
    question_count: int = 3

class MockInterviewSubmitAnswer(BaseModel):
    session_id: int
    response_text: str

class MockInterviewResponseOut(BaseModel):
    id: int
    question_text: str
    category: str
    student_response: str
    score: Optional[float]
    evaluation_status: str
    strengths: List[str]
    missing_concepts: List[str]
    improvement_suggestions: List[str]
    sample_answer: str
    ai_engine: str

class MockInterviewDetail(BaseModel):
    id: int
    category: str
    target_role: str
    difficulty: str
    total_questions: int
    completed_questions: int
    status: str
    current_question_text: Optional[str] = None
    questions: Optional[List[Dict[str, Any]]] = None
    responses: List[MockInterviewResponseOut]
    overall_score: Optional[float] = None
    feedback_summary: Optional[str] = None

# --- Resume Schemas ---

class ResumeUpdate(BaseModel):
    title: Optional[str] = "Placement Resume"
    full_name: str
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    target_role: Optional[str] = None
    summary: Optional[str] = None
    education_json: List[Dict[str, Any]] = []
    skills_json: List[str] = []
    projects_json: List[Dict[str, Any]] = []
    experience_json: List[Dict[str, Any]] = []
    certifications_json: List[Dict[str, Any]] = []
    links_json: Dict[str, str] = {}

class ResumeOut(BaseModel):
    id: int
    title: str
    full_name: str
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    target_role: Optional[str] = None
    summary: Optional[str] = None
    education_json: List[Dict[str, Any]]
    skills_json: List[str]
    projects_json: List[Dict[str, Any]]
    experience_json: List[Dict[str, Any]]
    certifications_json: List[Dict[str, Any]]
    links_json: Dict[str, str]
    ai_review_feedback: Optional[Dict[str, Any]] = None
    updated_at: datetime

    class Config:
        from_attributes = True

# --- Bookmarks & Progress Schemas ---

class BookmarkCreate(BaseModel):
    item_type: str
    item_id: int
    title: str
    topic_name: Optional[str] = None
    category: Optional[str] = None
    link_path: str

class BookmarkOut(BaseModel):
    id: int
    item_type: str
    item_id: int
    title: str
    topic_name: Optional[str] = None
    category: Optional[str] = None
    link_path: str
    created_at: datetime

    class Config:
        from_attributes = True

class DashboardStats(BaseModel):
    total_questions_attempted: int
    overall_accuracy_percentage: float
    total_lessons_completed: int
    total_coding_solved: int
    total_mock_interviews: int
    streak_days: int
    recent_activities: List[Dict[str, Any]]
    weak_topics: List[Dict[str, Any]]
    strong_topics: List[Dict[str, Any]]
    recommended_activities: List[Dict[str, Any]]
    roadmap_progress_percentage: float
    target_role: str
    skill_level: str

# --- Learning Resources & Topics ---

class LearningResourceOut(BaseModel):
    id: int
    title: str
    url: str
    resource_type: str
    provider_name: str
    language: str
    description: str
    is_verified: bool

    class Config:
        from_attributes = True

class LessonDetail(BaseModel):
    id: int
    topic_id: int
    title: str
    slug: str
    difficulty: str
    content_markdown: str
    key_takeaways: List[str]
    estimated_minutes: int
    is_completed: bool = False
    resources: List[LearningResourceOut] = []

    class Config:
        from_attributes = True

class TopicDetail(BaseModel):
    id: int
    name: str
    slug: str
    category: str
    subcategory: str
    description: str
    icon: str
    lessons: List[Dict[str, Any]]
    resources: List[LearningResourceOut]
    question_count: int
    coding_count: int

    class Config:
        from_attributes = True
