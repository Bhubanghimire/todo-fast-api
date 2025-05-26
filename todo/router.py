from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from todo.models import TODO
from todo.schemas import TodoSchamas

todo_router = APIRouter()


@todo_router.get("/", response_model=List[TodoSchamas])
async def todo_list(db: Session = Depends(get_db)):
    todos_query = db.query(TODO)
    return todos_query


@todo_router.get("/done", response_model=List[TodoSchamas])
async def list_done_todo(db: Session = Depends(get_db)):
    query = db.query(TODO)
    done_todos = query.filter(TODO.is_done == True)
    return done_todos.all()


@todo_router.post("/create", response_model=TodoSchamas)
async def todo_create(text: str, is_complete: bool = False, db: Session = Depends(get_db)):
    todo = TODO(text=text, is_done=is_complete)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@todo_router.put("/update/{id}")
async def todo_update(id: int, new_text: str, is_done: bool, db: Session = Depends(get_db)):
    todo_query = db.query(TODO).filter(TODO.id == id)
    todo = todo_query.first()
    if new_text:
        todo.text = new_text
    todo.is_complete = is_done
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@todo_router.delete("/delete/{id}")
async def delete_todo(id: int, db: Session = Depends((get_db))):
    todo = db.query(TODO).filter(TODO.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()

    return {"message": "Todo deleted"}
