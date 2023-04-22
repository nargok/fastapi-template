from fastapi import FastAPI, Query, Path, Body, HTTPException, Depends
from pydantic import BaseModel, Field
from enum import Enum
from typing import Union, Annotated
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Tags(str, Enum):
    item = "Item"
    user = "User"


class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: str | None 
    price: float
    tax: float | None = None

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "foo",
    #             "description": "a very nice item",
    #             "price": 35.4,
    #             "tax": 3.2,
    #         }
    #     }


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return { "q": q, "skip": skip, "limit": limit }


CommonsDep = Annotated[dict, Depends(common_parameters)]


class CommonQueryParams:
    def __init__(self, q: str | None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/")
async def root():
    return { "greeting": "Hello world "}


@app.get("/items/", tags = [Tags.item])
async def list_item(commons: Annotated[CommonQueryParams, Depends()]):
    return [
        Item(name="hoge", price=35.4 ),
        Item(name="fuga", price=35.4 ),
    ]


@app.get("/items/{item_id}", tags = [Tags.item])
def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
     q: Union[str, None] = Query(default=None, min_length=3, max_length=10)
):
    items = { "foo": "Foo Bar"}
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    return { "item_id": item_id, "q": q}


@app.post("/items", tags = [Tags.item])
async def create_item(item: Item) -> Item:
    return item


class User(BaseModel):
    id: int
    name: str

@app.get("/users", tags=[Tags.user], response_model=list[User])
async def list_user(commons: CommonsDep):
    return [
        User(1, "hoge"),
        User(2, "fuga")
    ]


@app.put("/items/{item_id}", tags = [Tags.item])
def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    return { "item_name": item.name, "item_id": item_id }


@app.post("/users", tags=[Tags.user])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/uesrs/me", tags=[Tags.user])
async def read_user_me():
    return { "user_id": "the current user" }


@app.get("/users/{user_id}", tags=[Tags.user], response_model=schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_user(db=db, user_id=user_id)


class ModelName(str, Enum):
    alexnet = "alexnet"
    test = "test"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == 'test':
        return { "model_name": model_name, "message": "test" }
    
    return { "model_name": model_name, "message": "No name" }
    
