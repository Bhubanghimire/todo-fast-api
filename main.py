from fastapi import FastAPI
from app.todo.router import todo_router
from app.core.database import Base, engine

# 👇 Import model files (but NOT using *)
import app.todo.models
import app.account.models

app = FastAPI()

app.include_router(todo_router, prefix="/todo", tags=["todo"])

# 👇 Create DB tables after importing models
Base.metadata.create_all(bind=engine)
