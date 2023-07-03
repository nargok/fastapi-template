from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependency.usecase import user_usecase

from app.presentation.form.user import UserCreateModel, UserReadModel
from app.usecase.user import UserUseCase


from app.dependency.repository import user_repository

router = APIRouter(
    prefix='/users',
    tags=["users"],
)

@router.post("/")
def create_user(
    user: UserCreateModel,
    useCase: UserUseCase = Depends(user_usecase)
):
    # db_user = useCase.get_by_email(email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return useCase.register(user=user)


@router.get("/me")
async def read_user_me():
    return { "user_id": "the current user" }


@router.get("/{user_id}", response_model=UserReadModel)
def read_user(
    user_id: str,
    useCase: UserUseCase = Depends(user_usecase)
):
    user = useCase.get(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
