
from abc import ABC, abstractmethod
from app.domain.user.user import UserModel

from app.schemas import UserCreate


class UserReposigoty(ABC):
    @abstractmethod
    def create_user(self, user: UserCreate) -> UserModel:
        raise NotImplementedError
    

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserModel | None:
        raise NotImplementedError
    

    def get_user(self, user_id: int) -> UserModel | None:
        raise NotImplementedError
