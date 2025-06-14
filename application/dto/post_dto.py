from dataclasses import dataclass
from datetime import datetime


@dataclass
class PostCreateDTO:
    title: str
    content: str
    author_id: int


@dataclass
class PostDTO:
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime