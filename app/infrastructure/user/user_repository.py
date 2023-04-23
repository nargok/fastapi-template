from app.domain.user.user_repository import UserRepository
from app.infrastructure.repository.base import BaseRepository

from app.schemas import UserCreate
from app.infrastructure.user.user_dto import User

class UserRepositoryImpl(BaseRepository, UserRepository):
    def create_user(self, *,  user: UserCreate):
        fakse_hashed_password = user.password + "notreallyhashed"
        db_user = User(email=user.email, hashed_password=fakse_hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user


    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

        
    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

# TODO model変換