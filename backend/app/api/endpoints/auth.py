from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
import datetime
from app.core.database import get_db
from app.core.config import settings
from app.core.security import (
    get_password_hash, verify_password, create_access_token,
    generate_secure_random_token, hash_token
)
from app.models.models import User, UserProfile, Resume, AuthSession, PasswordResetToken, utc_now
from app.schemas.schemas import (
    UserRegister, UserLogin, Token, UserOut,
    ForgotPasswordRequest, ForgotPasswordResponse, ResetPasswordRequest
)
from app.api.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

def set_auth_cookies(response: Response, raw_token: str, remember_me: bool = False):
    max_age = (30 * 24 * 3600) if remember_me else (settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    response.set_cookie(
        key=settings.SESSION_COOKIE_NAME,
        value=raw_token,
        max_age=max_age,
        httponly=True,
        secure=settings.COOKIE_SECURE,
        samesite=settings.COOKIE_SAMESITE,
        path="/"
    )
    # Anti-CSRF token readable by frontend JavaScript
    csrf_token = generate_secure_random_token(16)
    response.set_cookie(
        key=settings.CSRF_COOKIE_NAME,
        value=csrf_token,
        max_age=max_age,
        httponly=False,
        secure=settings.COOKIE_SECURE,
        samesite=settings.COOKIE_SAMESITE,
        path="/"
    )

def clear_auth_cookies(response: Response):
    response.delete_cookie(key=settings.SESSION_COOKIE_NAME, path="/")
    response.delete_cookie(key=settings.CSRF_COOKIE_NAME, path="/")

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(
    user_in: UserRegister,
    response: Response,
    request: Request,
    db: Session = Depends(get_db)
):
    normalized_email = user_in.email.lower().strip()
    existing = db.query(User).filter(User.email == normalized_email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email address already exists."
        )

    resolved_name = (user_in.full_name or user_in.name or "").strip()
    if not resolved_name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Full name is required."
        )

    # Public registration is strictly "student" role
    user = User(
        email=normalized_email,
        hashed_password=get_password_hash(user_in.password),
        full_name=resolved_name,
        role="student",
        is_active=True,
        is_verified=True,
        last_login_at=utc_now()
    )
    db.add(user)
    db.flush()

    # Create profile with user-selected target role
    initial_role = (user_in.target_role or "Software Developer").strip()
    profile = UserProfile(
        user_id=user.id,
        course="B.Tech Computer Science",
        study_year="3rd Year",
        target_role=initial_role,
        preferred_programming_language="Python",
        skill_level="Beginner",
        study_availability=2.5,
        preferred_topics=["Data Structures", "Aptitude", "SQL"],
        prep_priorities=["Campus Placement", "Product Companies"],
        onboarding_completed=False
    )
    db.add(profile)

    # Create blank resume
    resume = Resume(
        user_id=user.id,
        title="Placement Resume",
        full_name=user.full_name,
        email=user.email,
        education_json=[{
            "degree": "B.Tech in Computer Science",
            "institution": "University / College",
            "year": "2023 - 2027",
            "score": "8.5 CGPA"
        }],
        skills_json=["Python", "SQL", "Data Structures", "Git"],
        projects_json=[],
        experience_json=[],
        certifications_json=[],
        links_json={}
    )
    db.add(resume)

    # Create database session
    raw_token = generate_secure_random_token(32)
    session_hash = hash_token(raw_token)
    expires = utc_now() + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    auth_sess = AuthSession(
        user_id=user.id,
        session_token_hash=session_hash,
        user_agent=request.headers.get("user-agent", "")[:250],
        ip_address=request.client.host if request.client else "",
        expires_at=expires,
        is_revoked=False
    )
    db.add(auth_sess)
    db.commit()
    db.refresh(user)
    if user.profile:
        db.refresh(user.profile)

    set_auth_cookies(response, raw_token, remember_me=False)
    jwt_token = create_access_token(user.id)
    return Token(access_token=jwt_token, token_type="bearer", user=UserOut.model_validate(user))

@router.post("/login", response_model=Token)
def login(
    user_in: UserLogin,
    response: Response,
    request: Request,
    db: Session = Depends(get_db)
):
    normalized_email = user_in.email.lower().strip()
    user = db.query(User).filter(User.email == normalized_email).first()
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password."
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Your account has been deactivated. Please contact support."
        )

    user.last_login_at = utc_now()

    # Create session token
    raw_token = generate_secure_random_token(32)
    session_hash = hash_token(raw_token)
    days = 30 if user_in.remember_me else 7
    expires = utc_now() + datetime.timedelta(days=days)

    auth_sess = AuthSession(
        user_id=user.id,
        session_token_hash=session_hash,
        user_agent=request.headers.get("user-agent", "")[:250],
        ip_address=request.client.host if request.client else "",
        expires_at=expires,
        is_revoked=False
    )
    db.add(auth_sess)
    db.commit()
    db.refresh(user)
    if user.profile:
        db.refresh(user.profile)

    set_auth_cookies(response, raw_token, remember_me=bool(user_in.remember_me))
    jwt_token = create_access_token(user.id, expires_delta=datetime.timedelta(days=days))
    return Token(access_token=jwt_token, token_type="bearer", user=UserOut.model_validate(user))

@router.post("/logout")
def logout(
    request: Request,
    response: Response,
    db: Session = Depends(get_db)
):
    # Invalidate session in database
    session_cookie = request.cookies.get(settings.SESSION_COOKIE_NAME)
    if session_cookie:
        session_hash = hash_token(session_cookie)
        db_sess = db.query(AuthSession).filter(AuthSession.session_token_hash == session_hash).first()
        if db_sess:
            db_sess.is_revoked = True
            db.commit()

    clear_auth_cookies(response)
    return {"message": "Successfully logged out. Session invalidated."}

@router.get("/me", response_model=UserOut)
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return UserOut.model_validate(current_user)

@router.post("/forgot-password", response_model=ForgotPasswordResponse)
def forgot_password(payload: ForgotPasswordRequest, db: Session = Depends(get_db)):
    normalized_email = payload.email.lower().strip()
    user = db.query(User).filter(User.email == normalized_email).first()

    reset_token = None
    if user and user.is_active:
        raw_reset_token = generate_secure_random_token(32)
        token_hash = hash_token(raw_reset_token)
        expires = utc_now() + datetime.timedelta(hours=1)

        db_token = PasswordResetToken(
            user_id=user.id,
            token_hash=token_hash,
            expires_at=expires
        )
        db.add(db_token)
        db.commit()
        reset_token = raw_reset_token

    return ForgotPasswordResponse(
        message="If an account exists with this email address, password reset instructions have been generated.",
        reset_token=reset_token
    )

@router.post("/reset-password")
def reset_password(payload: ResetPasswordRequest, db: Session = Depends(get_db)):
    token_hash = hash_token(payload.token.strip())
    now = utc_now()
    db_token = db.query(PasswordResetToken).filter(
        PasswordResetToken.token_hash == token_hash,
        PasswordResetToken.used_at == None
    ).first()

    if not db_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or already used password reset token."
        )

    expires_at = db_token.expires_at
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=datetime.timezone.utc)
    if expires_at < now:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password reset token has expired."
        )

    user = db.query(User).filter(User.id == db_token.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User account not found.")

    user.hashed_password = get_password_hash(payload.new_password)
    db_token.used_at = now

    # Revoke all previous active auth sessions for security
    active_sessions = db.query(AuthSession).filter(
        AuthSession.user_id == user.id,
        AuthSession.is_revoked == False
    ).all()
    for s in active_sessions:
        s.is_revoked = True

    db.commit()
    return {"message": "Password successfully reset. Please log in with your new password."}
