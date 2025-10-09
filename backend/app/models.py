from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Todo:
    id: int
    title: str
    done: bool = False
    created_at: datetime = datetime.utcnow()
    description: Optional[str] = None
