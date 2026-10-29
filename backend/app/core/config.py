from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "InterviewAI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Auth & Secret keys
    AUTH_SECRET_KEY: str = "interviewai-super-secret-key-for-development-change-in-production-2026"
    SECRET_KEY: str = "interviewai-super-secret-key-for-development-change-in-production-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Cookie security
    SESSION_COOKIE_NAME: str = "interviewai_session"
    CSRF_COOKIE_NAME: str = "interviewai_csrf"
    COOKIE_SECURE: bool = False  # Set to True in HTTPS production
    COOKIE_SAMESITE: str = "lax"
    
    # URLs
    FRONTEND_URL: str = "http://localhost:5173"
    BACKEND_URL: str = "http://localhost:8000"

    # Database
    DATABASE_URL: str = "sqlite:///./interviewai.db"

    # AI Configuration
    AI_PROVIDER: Optional[str] = None
    AI_MODEL: Optional[str] = "gemini-1.5-flash"
    AI_API_KEY: Optional[str] = None

    # Email Service (Optional)
    EMAIL_PROVIDER: Optional[str] = None
    EMAIL_API_KEY: Optional[str] = None

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()
