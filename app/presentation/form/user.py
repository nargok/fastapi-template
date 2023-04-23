from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserReadModel(UserBase):
    id: int
    is_active: bool


class UserCreateModel(UserBase):
    password: str
