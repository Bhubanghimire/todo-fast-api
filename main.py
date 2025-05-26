from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session

from todo.router import todo_router

# from . import crud, models, schemas
# from .database import SessionLocal, engine, get_db

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router, prefix="/todo", tags=["Blog"])

# import uvicorn
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)