from abc import ABC, abstractmethod

from app.domain.user.user import UserModel
from app.domain.user.user_repository import UserRepository
from app.presentation.form.user import UserCreateModel, UserReadModel


class UserUseCase(ABC):
    @abstractmethod
    def get(self, user_id: int) -> UserReadModel:
        raise NotImplementedError()
    
    def get_by_email(self, email: str) -> UserModel:
        raise NotImplementedError()

    @abstractmethod    
    def register() -> UserModel:
        raise NotImplementedError()
    


class UserUseCaseImpl(UserUseCase):
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get(self, user_id: int) -> UserReadModel:
        return self.__toResponse(self.repository.get_user(user_id))
    

    def get_by_email(self, email: str) -> UserModel:
        return self.__toResponse(self.repository.get_user_by_email(email=email))
    

    def register(self, user: UserCreateModel) -> UserModel:
        # return self.repository.create_user(user=user)
        return self.repository.save(user=user)
    

    def __toResponse(self, user: UserModel) -> UserReadModel:
        return UserReadModel(
            id=user.id,
            email=user.email,
            is_active=user.is_active,
        )

