from abc import ABC, abstractmethod
from typing import Optional


class BaseRepository(ABC):
    @abstractmethod
    def create(self, item, **kwargs):
        pass

    @abstractmethod
    def update(self, id: str, item, **kwargs):
        pass

    @abstractmethod
    def delete(self, id: str, **kwargs):
        pass

    @abstractmethod
    def get_by_id(self, id: str, **kwargs):
        pass

    @abstractmethod
    def get_and_count(self, filter: Optional[dict], **kwargs):
        pass
