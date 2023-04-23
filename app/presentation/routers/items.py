
from typing import Annotated, Union
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query

from app.infrastructure.item.item_repository import ItemRepository
from app.dependency.repository import get_repository
from app.dependency.request import CommonsDep

from app.schemas import Item


router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/")
async def list_item(
    commons: CommonsDep,
    repository: ItemRepository = Depends(get_repository(ItemRepository))
):
    return repository.list_items(skip=commons.skip, limit=commons.limit)


@router.get("/{item_id}")
def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
     q: Union[str, None] = Query(default=None, min_length=3, max_length=10)
):
    items = { "foo": "Foo Bar"}
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    return { "item_id": item_id, "q": q}


@router.post("/")
async def create_item(item: Item) -> Item:
    return item

@router.put("/{item_id}")
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