from app.domain.user.user import UserModel
from app.domain.user.user_repository import UserRepository
from app.infrastructure.repository.base import BaseRepository, db_persist

from app.infrastructure.user.user_dto import User
from app.presentation.form.user import UserCreateModel

class UserRepositoryImpl(UserRepository, BaseRepository):
    def create_user(self, *,  user: UserCreateModel):
        fakse_hashed_password = user.password + "notreallyhashed"
        db_user = User(email=user.email, hashed_password=fakse_hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user


    def get_user_by_email(self, email: str):
        db_user = self.db.query(User).filter(User.email == email).first()
        return self.__to_model(user=db_user)

        
    def get_user(self, user_id: int) -> UserModel:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        return self.__to_model(user=db_user)
    
    @db_persist
    def save(self, *,  user: UserCreateModel): # TODO userUpdateにも対応する
        fakse_hashed_password = user.password + "notreallyhashed"
        db_user = User(email=user.email, hashed_password=fakse_hashed_password)
        return self.db.merge(db_user)


    def __to_model(self, user: User) -> UserModel:
        return UserModel(
            id=user.id,
            email=user.email,
            is_active=user.is_active,
        )
