from typing import List
from uuid import UUID

from app.api.v1.user import UserAPI
from app.schemas import CreateUserSchema, ReadUserSchema, UpdateUserSchema

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/", response_model=List[ReadUserSchema])
async def gets(request: Request) -> List[ReadUserSchema]:
    return UserAPI.gets(request)


@router.get("/{uuid}", response_model=ReadUserSchema)
async def get(request: Request, uuid: UUID) -> ReadUserSchema:
    return UserAPI.get(request, uuid)


@router.post("/", response_model=CreateUserSchema)
async def create(request: Request, schema: CreateUserSchema) -> CreateUserSchema:
    return UserAPI.create(request, schema)


@router.put("/{uuid}/", response_model=UpdateUserSchema)
async def update(
    request: Request, uuid: UUID, schema: UpdateUserSchema
) -> UpdateUserSchema:
    return UserAPI.update(request, uuid, schema)


@router.delete("/{uuid}/")
async def delete(request: Request, uuid: UUID) -> None:
    return UserAPI.delete(request, uuid)
