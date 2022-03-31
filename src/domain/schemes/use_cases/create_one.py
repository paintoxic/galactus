from fastapi import HTTPException
from domain.schemes.models.scheme_dom import SchemesDOM
from packages.storage.repository.base import BaseRepository


class CreateOne(object):
    def __init__(self, repository: BaseRepository) -> None:
        self._repo = repository

    def execute(self, item: SchemesDOM):
        _, count = self._repo.get_and_count({"name": item.name})
        if count > 0:
            raise HTTPException(status_code=400, detail="Scheme already exist")
        inserted_id = self._repo.create(item)
        return self._repo.get_by_id(inserted_id)
