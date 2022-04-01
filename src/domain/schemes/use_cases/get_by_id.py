from fastapi import HTTPException
from packages.storage.repository.base import BaseRepository


class GetById(object):
    def __init__(self, repository: BaseRepository) -> None:
        self._repo = repository

    def execute(self, id: str):
        response = self._repo.get_by_id(id)
        if response is None:
            raise HTTPException(status_code=404, detail="Scheme not found")
        return response
