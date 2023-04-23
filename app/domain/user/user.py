class UserModel():
    def __init__(self, id: int, email: str, is_active: bool):
        self.id = id
        self.email = email
        self.is_active = is_active
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, UserModel):
            return self.id == o.id
        
        return False
