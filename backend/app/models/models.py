import datetime
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Float, JSON, Index
)
from sqlalchemy.orm import relationship
from app.core.database import Base

def utc_now():
    return datetime.datetime.now(datetime.timezone.utc)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(String(50), default="student", nullable=False)  # "student", "admin"
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=True, nullable=False)
    last_login_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    auth_sessions = relationship("AuthSession", back_populates="user", cascade="all, delete-orphan")
    reset_tokens = relationship("PasswordResetToken", back_populates="user", cascade="all, delete-orphan")
    practice_sessions = relationship("PracticeSession", back_populates="user", cascade="all, delete-orphan")
    submitted_answers = relationship("SubmittedAnswer", back_populates="user", cascade="all, delete-orphan")
    coding_submissions = relationship("CodingSubmission", back_populates="user", cascade="all, delete-orphan")
    interview_sessions = relationship("InterviewSession", back_populates="user", cascade="all, delete-orphan")
    resume = relationship("Resume", back_populates="user", uselist=False, cascade="all, delete-orphan")
    bookmarks = relationship("Bookmark", back_populates="user", cascade="all, delete-orphan")
    lesson_progress = relationship("LessonProgress", back_populates="user", cascade="all, delete-orphan")
    activities = relationship("ActivityEvent", back_populates="user", cascade="all, delete-orphan")
    communication_sessions = relationship("CommunicationSession", back_populates="user", cascade="all, delete-orphan")

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    college = Column(String(255), nullable=True)
    course = Column(String(255), nullable=True)          # mapped to degree / course
    study_year = Column(String(50), nullable=True)       # mapped to graduation year / year of study
    target_role = Column(String(100), default="Software Developer", nullable=False)
    preferred_programming_language = Column(String(50), default="Python", nullable=False)
    skill_level = Column(String(50), default="Beginner", nullable=False)  # Beginner, Intermediate, Advanced
    study_availability = Column(Float, default=2.0, nullable=False)       # study hours per day
    preferred_topics = Column(JSON, default=list, nullable=False)
    prep_priorities = Column(JSON, default=list, nullable=False)
    onboarding_completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    user = relationship("User", back_populates="profile")

class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token_hash = Column(String(255), unique=True, index=True, nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=False)
    used_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="reset_tokens")

class AuthSession(Base):
    __tablename__ = "auth_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    session_token_hash = Column(String(255), unique=True, index=True, nullable=False)
    user_agent = Column(String(255), nullable=True)
    ip_address = Column(String(100), nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=False)
    is_revoked = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="auth_sessions")

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(String(50), default="BookOpen", nullable=False)

    topics = relationship("Topic", back_populates="subject", cascade="all, delete-orphan")

class LearningPath(Base):
    __tablename__ = "learning_paths"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(String(50), default="Code2", nullable=False)
    estimated_weeks = Column(Integer, default=12, nullable=False)
    difficulty = Column(String(50), default="All Levels", nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    stages = relationship("RoadmapStage", back_populates="path", order_by="RoadmapStage.stage_number", cascade="all, delete-orphan")

class RoadmapStage(Base):
    __tablename__ = "roadmap_stages"

    id = Column(Integer, primary_key=True, index=True)
    path_id = Column(Integer, ForeignKey("learning_paths.id", ondelete="CASCADE"), nullable=False)
    stage_number = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    estimated_hours = Column(Integer, default=10, nullable=False)
    skills_covered = Column(JSON, default=list, nullable=False)
    stage_type = Column(String(50), default="core", nullable=False)  # core, elective, capstone

    path = relationship("LearningPath", back_populates="stages")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="SET NULL"), nullable=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    category = Column(String(50), index=True, nullable=False)  # aptitude, technical, coding, soft_skills
    subcategory = Column(String(100), index=True, nullable=False)  # quantitative, logical, verbal, programming, web_dev, cs
    description = Column(Text, nullable=False)
    icon = Column(String(50), default="BookOpen", nullable=False)

    subject = relationship("Subject", back_populates="topics")
    lessons = relationship("Lesson", back_populates="topic", cascade="all, delete-orphan")
    resources = relationship("LearningResource", back_populates="topic", cascade="all, delete-orphan")
    questions = relationship("Question", back_populates="topic", cascade="all, delete-orphan")
    coding_problems = relationship("CodingProblem", back_populates="topic", cascade="all, delete-orphan")

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    difficulty = Column(String(50), default="Beginner", nullable=False)  # Beginner, Intermediate, Advanced
    content_markdown = Column(Text, nullable=False)
    key_takeaways = Column(JSON, default=list, nullable=False)
    estimated_minutes = Column(Integer, default=15, nullable=False)
    order_index = Column(Integer, default=1, nullable=False)
    is_published = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    topic = relationship("Topic", back_populates="lessons")
    progress_records = relationship("LessonProgress", back_populates="lesson", cascade="all, delete-orphan")

class LearningResource(Base):
    __tablename__ = "learning_resources"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    url = Column(String(500), nullable=False)
    resource_type = Column(String(50), default="documentation", nullable=False)  # documentation, article, video, practice
    provider_name = Column(String(100), nullable=False)
    language = Column(String(50), default="English", nullable=False)
    description = Column(Text, nullable=False)
    is_verified = Column(Boolean, default=True, nullable=False)

    topic = relationship("Topic", back_populates="resources")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    question_type = Column(String(50), default="aptitude_mcq", nullable=False)  # aptitude_mcq, technical_mcq, interview_q
    difficulty = Column(String(50), default="intermediate", nullable=False)  # beginner, intermediate, advanced
    question_text = Column(Text, nullable=False)
    code_snippet = Column(Text, nullable=True)
    
    # Detailed feedback elements for the "Learn from every answer" core feature
    explanation = Column(Text, nullable=False)
    step_by_step_reasoning = Column(Text, nullable=False)
    practical_example = Column(Text, nullable=False)
    common_mistake = Column(Text, nullable=False)
    learning_tip = Column(Text, nullable=False)
    related_concept_url = Column(String(500), nullable=True)
    is_published = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    topic = relationship("Topic", back_populates="questions")
    options = relationship("QuestionOption", back_populates="question", cascade="all, delete-orphan", order_by="QuestionOption.option_key")
    session_questions = relationship("SessionQuestion", back_populates="question")
    submitted_answers = relationship("SubmittedAnswer", back_populates="question")

class QuestionOption(Base):
    __tablename__ = "question_options"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    option_key = Column(String(10), nullable=False)  # "A", "B", "C", "D"
    option_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    why_wrong_explanation = Column(Text, nullable=True)  # Kept on backend, shown after submission

    question = relationship("Question", back_populates="options")

class PracticeSession(Base):
    __tablename__ = "practice_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(50), nullable=False)  # aptitude, technical
    subcategory = Column(String(100), nullable=True)
    difficulty = Column(String(50), default="all", nullable=False)
    session_mode = Column(String(50), default="practice", nullable=False)  # practice, timed, mock_placement, daily_challenge, weak_topic
    time_limit_seconds = Column(Integer, nullable=True)
    marked_for_review_json = Column(JSON, default=list, nullable=False)
    total_questions = Column(Integer, default=5, nullable=False)
    completed_questions = Column(Integer, default=0, nullable=False)
    correct_count = Column(Integer, default=0, nullable=False)
    score_percentage = Column(Float, default=0.0, nullable=False)
    status = Column(String(50), default="in_progress", nullable=False)  # in_progress, completed
    started_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="practice_sessions")
    session_questions = relationship("SessionQuestion", back_populates="session", cascade="all, delete-orphan", order_by="SessionQuestion.order_index")

class SessionQuestion(Base):
    __tablename__ = "session_questions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("practice_sessions.id", ondelete="CASCADE"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    order_index = Column(Integer, nullable=False)
    is_answered = Column(Boolean, default=False, nullable=False)
    submitted_answer = Column(String(10), nullable=True)
    is_correct = Column(Boolean, nullable=True)
    answered_at = Column(DateTime(timezone=True), nullable=True)

    session = relationship("PracticeSession", back_populates="session_questions")
    question = relationship("Question", back_populates="session_questions")

class SubmittedAnswer(Base):
    __tablename__ = "submitted_answers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    session_id = Column(Integer, ForeignKey("practice_sessions.id", ondelete="SET NULL"), nullable=True)
    selected_option = Column(String(10), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="submitted_answers")
    question = relationship("Question", back_populates="submitted_answers")

class CodingProblem(Base):
    __tablename__ = "coding_problems"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    difficulty = Column(String(50), default="Easy", nullable=False)  # Easy, Medium, Hard
    category = Column(String(100), nullable=False)  # Arrays, Strings, Trees, DP, etc.
    description = Column(Text, nullable=False)
    input_format = Column(Text, nullable=False)
    output_format = Column(Text, nullable=False)
    constraints = Column(Text, nullable=False)
    sample_input = Column(Text, nullable=False)
    sample_output = Column(Text, nullable=False)
    test_cases_json = Column(JSON, default=list, nullable=False)
    starter_code_python = Column(Text, nullable=False)
    starter_code_javascript = Column(Text, nullable=False)
    starter_code_java = Column(Text, nullable=False)
    starter_code_cpp = Column(Text, nullable=False)
    solution_explanation = Column(Text, nullable=False)
    time_complexity = Column(String(100), nullable=False)
    space_complexity = Column(String(100), nullable=False)
    hints = Column(JSON, default=list, nullable=False)
    external_url = Column(String(500), nullable=True)
    external_platform = Column(String(100), nullable=True)

    topic = relationship("Topic", back_populates="coding_problems")
    submissions = relationship("CodingSubmission", back_populates="problem", cascade="all, delete-orphan")

class CodingSubmission(Base):
    __tablename__ = "coding_submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    problem_id = Column(Integer, ForeignKey("coding_problems.id", ondelete="CASCADE"), nullable=False)
    language = Column(String(50), nullable=False)
    code = Column(Text, nullable=False)
    status = Column(String(50), default="preview_evaluated", nullable=False)  # accepted, wrong_answer, preview_evaluated
    output_log = Column(Text, nullable=True)
    runtime_ms = Column(Integer, default=12, nullable=False)
    memory_kb = Column(Integer, default=1024, nullable=False)
    submitted_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="coding_submissions")
    problem = relationship("CodingProblem", back_populates="submissions")

class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(100), default="Technical", nullable=False)
    target_role = Column(String(100), default="Software Developer", nullable=False)
    difficulty = Column(String(50), default="Medium", nullable=False)
    total_questions = Column(Integer, default=3, nullable=False)
    completed_questions = Column(Integer, default=0, nullable=False)
    overall_score = Column(Float, nullable=True)
    feedback_summary = Column(Text, nullable=True)
    status = Column(String(50), default="in_progress", nullable=False)  # in_progress, completed
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="interview_sessions")
    responses = relationship("InterviewResponse", back_populates="session", cascade="all, delete-orphan")

class InterviewResponse(Base):
    __tablename__ = "interview_responses"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id", ondelete="CASCADE"), nullable=False)
    question_text = Column(Text, nullable=False)
    category = Column(String(100), default="Technical", nullable=False)
    expected_aspects = Column(JSON, default=list, nullable=False)
    student_response = Column(Text, nullable=False)
    score = Column(Float, nullable=True)
    evaluation_status = Column(String(50), default="evaluated", nullable=False)
    strengths = Column(JSON, default=list, nullable=False)
    missing_concepts = Column(JSON, default=list, nullable=False)
    improvement_suggestions = Column(JSON, default=list, nullable=False)
    sample_answer = Column(Text, nullable=False)
    ai_engine = Column(String(100), default="InterviewAI Rule/Semantic Engine", nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    session = relationship("InterviewSession", back_populates="responses")

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    title = Column(String(255), default="My Placement Resume", nullable=False)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=True)
    location = Column(String(100), nullable=True)
    target_role = Column(String(100), nullable=True)
    summary = Column(Text, nullable=True)
    education_json = Column(JSON, default=list, nullable=False)
    skills_json = Column(JSON, default=list, nullable=False)
    projects_json = Column(JSON, default=list, nullable=False)
    experience_json = Column(JSON, default=list, nullable=False)
    certifications_json = Column(JSON, default=list, nullable=False)
    links_json = Column(JSON, default=dict, nullable=False)
    ai_review_feedback = Column(JSON, default=dict, nullable=True)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    user = relationship("User", back_populates="resume")

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    item_type = Column(String(50), nullable=False)  # question, coding_problem, lesson, resource
    item_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    topic_name = Column(String(100), nullable=True)
    category = Column(String(50), nullable=True)
    link_path = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="bookmarks")

class LessonProgress(Base):
    __tablename__ = "lesson_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(50), default="completed", nullable=False)
    completed_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="lesson_progress")
    lesson = relationship("Lesson", back_populates="progress_records")

class ActivityEvent(Base):
    __tablename__ = "activity_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    event_type = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False)
    details = Column(String(500), nullable=True)
    metadata_json = Column(JSON, default=dict, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="activities")

class CommunicationSession(Base):
    __tablename__ = "communication_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(100), default="Self Introduction", nullable=False)
    prompt_title = Column(String(255), nullable=False)
    prompt_question = Column(Text, nullable=False)
    framework = Column(Text, nullable=True)
    audio_filename = Column(String(255), nullable=True)
    audio_duration_seconds = Column(Float, default=0.0, nullable=False)
    transcript = Column(Text, nullable=False)
    overall_score = Column(Float, default=7.5, nullable=False)
    relevance_score = Column(Float, default=8.0, nullable=False)
    clarity_score = Column(Float, default=7.5, nullable=False)
    grammar_score = Column(Float, default=8.0, nullable=False)
    conciseness_score = Column(Float, default=7.0, nullable=False)
    delivery_score = Column(Float, default=7.0, nullable=False)
    wpm = Column(Integer, default=130, nullable=False)
    filler_words_count = Column(Integer, default=0, nullable=False)
    filler_words_list = Column(JSON, default=list, nullable=False)
    strengths = Column(JSON, default=list, nullable=False)
    improvements = Column(JSON, default=list, nullable=False)
    concepts_demonstrated = Column(JSON, default=list, nullable=True)
    concepts_missing = Column(JSON, default=list, nullable=True)
    follow_up_question = Column(Text, nullable=True)
    personalized_coaching = Column(Text, nullable=True)
    sample_answer = Column(Text, nullable=True)
    status = Column(String(50), default="completed", nullable=False)
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)

    user = relationship("User", back_populates="communication_sessions")
