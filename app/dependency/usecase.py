from fastapi import Depends
from app.dependency.repository import get_db, user_repository
from app.domain.user.user_repository import UserRepository
from app.infrastructure.user.user_repository import UserRepositoryImpl
from app.usecase.user import UserUseCase, UserUseCaseImpl
from sqlalchemy.orm import Session


def user_usecase(repository: UserRepository = Depends(user_repository)) -> UserUseCase:
    return UserUseCaseImpl(repository)
