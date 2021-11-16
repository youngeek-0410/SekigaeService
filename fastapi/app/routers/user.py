from typing import List
from uuid import UUID

import app.cruds.user as crud
from app.schemas import User as UserSchema
from db.database import get_db
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=List[UserSchema])
async def read_users(db: Session = Depends(get_db)):
    return crud.read_users(db=db)


@router.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: UUID, db: Session = Depends(get_db)):
    return crud.read_user(user_id=user_id, db=db)
