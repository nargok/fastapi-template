from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.user.user_repository import UserRepository

from .. import schemas, crud
from app.dependencies import get_repository

router = APIRouter(
    prefix='/users',
    tags=["users"],
)

@router.post("/")
def create_user(
    user: schemas.UserCreate,
    repository: UserRepository = Depends(get_repository(UserRepository))
):
    db_user = repository.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repository.create_user(user=user)


@router.get("/me")
async def read_user_me():
    return { "user_id": "the current user" }


@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: str,
    repository: UserRepository = Depends(get_repository(UserRepository))
):
    db_user = repository.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
