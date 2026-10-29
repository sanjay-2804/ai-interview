from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.models import User, Bookmark, utc_now
from app.schemas.schemas import BookmarkCreate, BookmarkOut
from app.api.deps import get_current_user

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])

@router.get("/", response_model=List[BookmarkOut])
def list_bookmarks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    bookmarks = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id
    ).order_by(Bookmark.created_at.desc()).all()
    return [BookmarkOut.model_validate(b) for b in bookmarks]

@router.post("/", response_model=BookmarkOut)
def toggle_bookmark(
    payload: BookmarkCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    existing = db.query(Bookmark).filter(
        Bookmark.user_id == current_user.id,
        Bookmark.item_type == payload.item_type,
        Bookmark.item_id == payload.item_id
    ).first()

    if existing:
        db.delete(existing)
        db.commit()
        return BookmarkOut(
            id=existing.id,
            item_type=existing.item_type,
            item_id=existing.item_id,
            title=existing.title,
            topic_name=existing.topic_name,
            category=existing.category,
            link_path=existing.link_path,
            created_at=existing.created_at
        )

    b = Bookmark(
        user_id=current_user.id,
        item_type=payload.item_type,
        item_id=payload.item_id,
        title=payload.title,
        topic_name=payload.topic_name,
        category=payload.category,
        link_path=payload.link_path,
        created_at=utc_now()
    )
    db.add(b)
    db.commit()
    db.refresh(b)
    return BookmarkOut.model_validate(b)

@router.delete("/{bookmark_id}")
def delete_bookmark(
    bookmark_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    b = db.query(Bookmark).filter(
        Bookmark.id == bookmark_id,
        Bookmark.user_id == current_user.id
    ).first()
    if not b:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bookmark not found or access denied."
        )
    db.delete(b)
    db.commit()
    return {"message": "Bookmark removed successfully."}
