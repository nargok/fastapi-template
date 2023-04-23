from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    descriptoin: str | None = None


class ItemCreateModel(BaseModel):
    price: float
    tax: float


class ItemReadModel(ItemBase):
    id: int
    owner_id: int
