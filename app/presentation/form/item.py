from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    descriptoin: str | None = None
