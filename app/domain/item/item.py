class ItemModel():
    def __init__(self, id: int):
        self.id = id
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, ItemModel):
            return self.id == o.id
    
        return False
