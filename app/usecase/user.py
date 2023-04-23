from abc import ABC, abstractmethod

from app.domain.user.user import UserModel
from app.domain.user.user_repository import UserRepository
from app.schemas import UserCreate


class UserUseCase(ABC):
    @abstractmethod
    def get(self, user_id: int) -> UserModel:
        raise NotImplementedError()
    
    def get_by_email(self, email: str) -> UserModel:
        raise NotImplementedError()

    @abstractmethod    
    def register() -> UserModel:
        raise NotImplementedError()
    


class UserUseCaseImpl(UserUseCase):
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get(self, user_id: int) -> UserModel:
        return self.repository.get_user(user_id)
    

    def get_by_email(self, email: str) -> UserModel:
        return self.repository.get_user_by_email(email=email)
    

    def register(self, user: UserCreate) -> UserModel:
        return self.repository.create_user(user=user)
