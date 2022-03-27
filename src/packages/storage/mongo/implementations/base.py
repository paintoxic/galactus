from abc import ABC, abstractmethod
from typing import Optional


class BaseMongoRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def get_and_count(self, filter: Optional[dict]):
        pass

    @abstractmethod
    def create(self, item):
        pass
