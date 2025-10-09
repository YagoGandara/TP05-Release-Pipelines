from pydantic import BaseModel, Field
from typing import Optional

class TodoIn(BaseModel):
    title: str = Field(min_length=1, max_length=140)
    description: Optional[str] = Field(default=None, max_length=500)

class TodoOut(BaseModel):
    id: int
    title: str
    done: bool
    description: Optional[str]
