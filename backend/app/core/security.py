import bcrypt
import jwt
import secrets
import hashlib
from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Union
from app.core.config import settings

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    except Exception:
        return False

def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    secret = settings.AUTH_SECRET_KEY or settings.SECRET_KEY
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, secret, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Optional[dict]:
    secret = settings.AUTH_SECRET_KEY or settings.SECRET_KEY
    try:
        decoded = jwt.decode(token, secret, algorithms=[settings.ALGORITHM])
        return decoded
    except jwt.PyJWTError:
        return None

def generate_secure_random_token(nbytes: int = 32) -> str:
    """Generates a cryptographically strong URL-safe random string."""
    return secrets.token_urlsafe(nbytes)

def hash_token(raw_token: str) -> str:
    """SHA-256 hash for database token storage."""
    return hashlib.sha256(raw_token.encode('utf-8')).hexdigest()
