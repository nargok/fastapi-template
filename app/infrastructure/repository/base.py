import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


logger = logging.getLogger('uvicorn')

# https://stackoverflow.com/questions/7889183/sqlalchemy-insert-or-update-example
def db_persist(func):
    def persit(*args, **kwargs):
        func(*args, **kwargs)
        # https://stackoverflow.com/questions/11731136/class-method-decorator-with-self-arguments
        db = args[0].db
        try:
            db.commit()
            logger.info("success calling db func: " + str(func))
            return True
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(e.args)
            return False
        finally:
            db.close()
    
    return persit

class BaseRepository:
    def __init__(self, db: Session) -> None:
        self.db = db
