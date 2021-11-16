from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    uuid: UUID
    username: str
    email: str
    uid: str

    class Config:
        orm_mode = True
