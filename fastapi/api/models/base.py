import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TIMESTAMP, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


class BaseModelMixin(Base):
    __abstract__ = True

    uuid = Column(
        VARCHAR(36),
        primary_key=True,
        server_default=uuid.uuid4().hex,
    )

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
