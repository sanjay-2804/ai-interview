from typing import Optional
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import datetime
from app.core.database import get_db
from app.core.security import decode_access_token, hash_token
from app.core.config import settings
from app.models.models import User, AuthSession, utc_now

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/token", auto_error=False)

def get_current_user(
    request: Request,
    token_header: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    # 1. Try to get token from HttpOnly cookie
    session_cookie = request.cookies.get(settings.SESSION_COOKIE_NAME)
    token = session_cookie or token_header

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required. Please sign in.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2. Check if token is an active database session
    token_hashed = hash_token(token)
    db_session = db.query(AuthSession).filter(
        AuthSession.session_token_hash == token_hashed,
        AuthSession.is_revoked == False
    ).first()

    if db_session:
        # Check expiry
        now = datetime.datetime.now(datetime.timezone.utc)
        expires_at = db_session.expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=datetime.timezone.utc)
        if expires_at < now:
            db_session.is_revoked = True
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session expired. Please sign in again.",
            )
        user = db.query(User).filter(User.id == db_session.user_id).first()
        if not user or not user.is_active:
            raise HTTPException(status_code=401, detail="User account is inactive or deleted.")
        return user

    # 3. Fallback: try decoding JWT access token
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User account is inactive or not found.",
        )
    return user

def get_current_admin(
    current_user: User = Depends(get_current_user)
) -> User:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator privileges required to access this resource."
        )
    return current_user

def get_optional_current_user(
    request: Request,
    token_header: Optional[str] = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> Optional[User]:
    try:
        return get_current_user(request, token_header, db)
    except HTTPException:
        return None
