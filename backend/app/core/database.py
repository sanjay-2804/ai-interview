import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

db_url = settings.DATABASE_URL

# In Vercel serverless environments, the root filesystem is read-only.
# Redirect SQLite database file to /tmp if using default local SQLite.
if os.environ.get("VERCEL"):
    if db_url.startswith("sqlite:///./") or db_url == "sqlite:///interviewai.db":
        db_url = "sqlite:////tmp/interviewai.db"

# Normalize PostgreSQL connection URLs to explicitly use psycopg2
# This seamlessly supports postgres:// and postgresql:// provided by Supabase, Neon, Render, Railway, etc.
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+psycopg2://", 1)
elif db_url.startswith("postgresql://") and not db_url.startswith("postgresql+"):
    db_url = db_url.replace("postgresql://", "postgresql+psycopg2://", 1)

engine_args = {}
if db_url.startswith("sqlite"):
    engine_args["connect_args"] = {"check_same_thread": False}
else:
    # Serverless pooling optimizations for remote PostgreSQL
    engine_args["pool_pre_ping"] = True
    engine_args["pool_recycle"] = 300

engine = create_engine(
    db_url,
    **engine_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
