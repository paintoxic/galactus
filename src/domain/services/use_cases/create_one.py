from domain.services.models.service_dom import ServiceDOM
from fastapi import HTTPException
from packages.storage.repository.base import BaseRepository


class CreateOne(object):
    def __init__(self, repository: BaseRepository, schemes_repo: BaseRepository) -> None:
        self._repo = repository
        self._schemes_repo = schemes_repo

    def execute(self, item: ServiceDOM):
        self._validate(item)
        inserted_id = self._repo.create(item)
        return self._repo.get_by_id(inserted_id)

    def _validate(self, item: ServiceDOM):
        _, count = self._repo.get_and_count({"name": item.name})
        if count > 0:
            raise HTTPException(status_code=400, detail="Scheme already exist")
        self._validate_main_scheme(item.main_scheme)
        self._validate_backends(item.backends)

    def _validate_main_scheme(self, main_scheme_id: str):
        main_scheme = self._schemes_repo.get_by_id(main_scheme_id)
        if main_scheme is None:
            raise HTTPException(
                status_code=404, detail="Main Scheme not found")

    def _validate_backends(self, backends: list):
        for item in backends:
            backend = self._schemes_repo.get_by_id(item)
            if backend is None:
                raise HTTPException(
                    status_code=404, detail=f'Backend not found ID : {item}')
