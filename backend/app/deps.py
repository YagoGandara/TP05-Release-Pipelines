import os
from typing import List
from .models import Todo

_TODOS: List[Todo] = []
_NEXT_ID = 1

class Store:
    def list(self) -> List[Todo]:
        return _TODOS

    def add(self, title: str, description: str | None = None) -> Todo:
        global _NEXT_ID
        todo = Todo(id=_NEXT_ID, title=title, description=description)
        _NEXT_ID += 1
        _TODOS.append(todo)
        return todo

    def health(self) -> dict:
        return {"status": "ok", "env": os.getenv("ENV", "unknown"), "app": os.getenv("APP_NAME", "api")}

def get_store() -> Store:
    return Store()
