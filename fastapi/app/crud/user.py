from ..models import User
from .base import BaseCRUD


class UserCRUD(BaseCRUD):
    model = User
