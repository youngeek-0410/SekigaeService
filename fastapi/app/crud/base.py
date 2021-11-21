from typing import List, TypeVar
from uuid import UUID

from sqlalchemy.orm import query, scoped_session

from ..db.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseCRUD:
    model: ModelType = None

    def __init__(self, db_session: scoped_session) -> None:
        self.db_session = db_session
        self.model.query = self.db_session.query_property()

    def get_query(self) -> query.Query:
        return self.model.query

    def gets(self) -> List[ModelType]:
        return self.get_query().all()

    def get_by_uuid(self, uuid: UUID) -> ModelType:
        return self.get_query().filter_by(uuid=uuid).first()

    def create(self, data: dict = {}) -> ModelType:
        obj = self.model()
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        self.db_session.add(obj)
        self.db_session.flush()
        self.db_session.refresh(obj)
        return obj

    def update(self, obj: ModelType, data: dict = {}) -> ModelType:
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        self.db_session.flush()
        self.db_session.refresh(obj)
        return obj

    def delete_by_uuid(self, uuid: UUID) -> None:
        obj = self.get_by_uuid(uuid)
        if obj:
            self.db_session.delete(obj)
            self.db_session.flush()
        return None
