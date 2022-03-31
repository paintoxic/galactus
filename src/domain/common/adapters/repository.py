
from typing import Optional
from packages.storage.repository.base import BaseRepository


class Repository(BaseRepository):
    def __init__(self, implementation: BaseRepository) -> None:
        self._implementation = implementation

    def get_by_id(self, id: str, **kwargs):
        return self._implementation.get_by_id(id, **kwargs)

    def get_and_count(self, filter: Optional[dict], **kwargs) -> list:
        return self._implementation.get_and_count(filter, **kwargs)

    def create(self, item, **kwargs):
        return self._implementation.create(item, **kwargs)

    def update(self, id: str, item, **kwargs):
        return self._implementation.update(id, item, **kwargs)

    def delete(self, id: str, **kwargs):
        return self._implementation.delete(id, **kwargs)
