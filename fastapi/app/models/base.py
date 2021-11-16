import uuid

from db.database import Base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.sql.functions import current_timestamp


class BaseModelMixin(Base):
    __abstract__ = True

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    created_at = Column(
        "created_at",
        TIMESTAMP(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
        comment="登録日時",
    )

    updated_at = Column(
        "updated_at",
        TIMESTAMP(timezone=True),
        onupdate=current_timestamp(),
        comment="最終更新日時",
    )

    # @declared_attr
    # def __mapper_args__(cls):
    #     return {'order_by': desc('updated_at')}
