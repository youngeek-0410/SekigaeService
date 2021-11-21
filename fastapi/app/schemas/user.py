from uuid import UUID

from pydantic import BaseModel


class BaseUserSchema(BaseModel):
    username: str
    email: str
    uid: str

    class Config:
        orm_mode = True


class CreateUserSchema(BaseUserSchema):
    pass


class UpdateUserSchema(BaseUserSchema):
    is_admin: bool


class ReadUserSchema(BaseUserSchema):
    uuid: UUID
