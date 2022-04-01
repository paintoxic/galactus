from typing import Optional

from packages.storage.repository.base import BaseRepository


class GetAndCount(object):
    def __init__(self, repository: BaseRepository) -> None:
        self._repo = repository

    def execute(self, filter: Optional[dict] = None):
        rows, count = self._repo.get_and_count(filter)
        return {"rows": rows, "count": count}
