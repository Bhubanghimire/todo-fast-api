from fastapi import FastAPI, Depends, HTTPException
from todo.router import todo_router


app = FastAPI()
app.include_router(todo_router, prefix="/todo", tags=["Blog"])

