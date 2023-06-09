from fastapi import FastAPI
from enum import Enum

from .infrastructure.database.config import engine, Base
from app.presentation.routers import users, items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
async def root():
    return { "greeting": "Hello world "}


class ModelName(str, Enum):
    alexnet = "alexnet"
    test = "test"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == 'test':
        return { "model_name": model_name, "message": "test" }
    
    return { "model_name": model_name, "message": "No name" }
