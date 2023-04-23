
from typing import Annotated, Type

from fastapi import Depends
from sqlalchemy.orm import Session
from app.domain.user.user_repository import UserRepository
from app.infrastructure.database.config import SessionLocal
from app.infrastructure.repository.base import BaseRepository
from app.infrastructure.user.user_repository import UserRepositoryImpl


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_repository(Repo_type: Type[BaseRepository]):
    def get_repo(db: Session = Depends(get_db)) -> Type[BaseRepository]:
        return Repo_type(db)
    return get_repo


def user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepositoryImpl(db)
    

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return { "q": q, "skip": skip, "limit": limit }


CommonsDep = Annotated[dict, Depends(common_parameters)]