from uuid import UUID

from app.models import User
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from fastapi import HTTPException


def read_users(db: Session):
    users = db.query(User).all()
    return users


def read_user(db: Session, user_id: UUID):
    try:
        user = db.query(User).get(user_id)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found.")
    return user
