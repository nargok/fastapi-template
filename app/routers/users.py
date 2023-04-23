from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependency.usecase import user_usecase

from app.domain.user.user_repository import UserRepository
from app.usecase.user import UserUseCase


from .. import schemas 
from app.dependency.repository import user_repository

router = APIRouter(
    prefix='/users',
    tags=["users"],
)

@router.post("/")
def create_user(
    user: schemas.UserCreate,
    useCase: UserUseCase = Depends(user_usecase)
):
    db_user = useCase.get_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return useCase.register(user=user)


@router.get("/me")
async def read_user_me():
    return { "user_id": "the current user" }


@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: str,
    useCase: UserUseCase = Depends(user_usecase)
):
    db_user = useCase.get(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
