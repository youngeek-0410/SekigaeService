from sqlalchemy import BOOLEAN, VARCHAR, Column, String

from ..models import BaseModelMixin


class User(BaseModelMixin):
    __tablename__ = "users"

    username = Column(VARCHAR(256), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    uid = Column(VARCHAR(128), nullable=False)

    is_admin = Column(BOOLEAN, nullable=False, default=False)
    is_active = Column(BOOLEAN, nullable=False, default=True)
