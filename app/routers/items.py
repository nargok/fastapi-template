
from typing import Annotated, Union
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from .. import schemas, crud
from app.dependencies import get_db, CommonsDep

from ..schemas import Item

# CommonQueryParams = Annotated[dict, Depends(common_parameters)]

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/items/")
async def list_item(commons: CommonsDep):
    return [
        Item(name="hoge", price=35.4 ),
        Item(name="fuga", price=35.4 ),
    ]


@router.get("/items/{item_id}")
def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
     q: Union[str, None] = Query(default=None, min_length=3, max_length=10)
):
    items = { "foo": "Foo Bar"}
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    return { "item_id": item_id, "q": q}


@router.post("/items")
async def create_item(item: Item) -> Item:
    return item

@router.put("/items/{item_id}")
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