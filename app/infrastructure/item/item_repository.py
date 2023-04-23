from app.infrastructure.repository.base import BaseRepository

from app.schemas import ItemCreate
from app.infrastructure.item.item_dto import Item

class ItemRepository(BaseRepository):
    def get_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(Item).offset(skip).limit(limit).all()


    def create_user_item(self, item: ItemCreate, user_id: int):
        db_item = Item(**item.dict(), owner_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
