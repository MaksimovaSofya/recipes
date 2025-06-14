from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.post import Post


class PostRepository(ABC):
    @abstractmethod
    def find_by_id(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    def find_all(self) -> List[Post]:
        pass

    @abstractmethod
    def find_by_author(self, author_id: int) -> List[Post]:
        pass

    @abstractmethod
    def save(self, post: Post) -> Post:
        pass

    @abstractmethod
    def delete(self, post_id: int) -> None:
        pass