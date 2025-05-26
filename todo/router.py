from fastapi import APIRouter

from database import session
from todo.models import TODO

todo_router = APIRouter()


@todo_router.get("/")
async def todo_list():
    todos_query = session.query(TODO)
    return {"todo_list": todos_query.all()}


@todo_router.post("/create")
async def todo_create(text=str, is_complete: bool = False):
    todo = TODO(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return {"todo added": todo}
