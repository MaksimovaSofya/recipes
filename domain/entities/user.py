from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from domain.entities.post import Post
    from domain.entities.comment import Comment


@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    password_hash: str
    created_at: datetime
    posts: List['Post'] = None
    comments: List['Comment'] = None

    def __post_init__(self):
        if self.posts is None:
            self.posts = []
        if self.comments is None:
            self.comments = []