from typing import Optional
from domain.services.models.service_dom import ServiceDOM
from packages.storage.mongo.implementations.models.service_dal import ServiceDAL
from packages.storage.repository.base import BaseRepository
from pymongo.database import Database

_COLLECTION_NAME = 'services'
_VIEW_NAME = 'services_populates'


class ServicesMongoImplementation(BaseRepository):
    def __init__(self, database: Database) -> None:
        self._collection = database.get_collection(_COLLECTION_NAME)
        self._view = database.get_collection(_VIEW_NAME)

    def get_by_id(self, id: str, **kwargs):
        response = self._view.find_one({"_id": id})
        return self._map_to_dom(response) if response is not None else None

    def get_and_count(self, filter: Optional[dict], **kwargs):
        rows = self._view.find(self._map_filter(filter))
        response = [self._map_to_dom(item) for item in rows]
        count = self._view.count_documents(self._map_filter(filter))
        return (response, count)

    def create(self, item, **kwargs):
        inserted = self._collection.insert_one(self._map_to_dal(item))
        return str(inserted.inserted_id)

    def update(self, id: str, item, **kwargs):
        pass

    def delete(self, id: str, **kwargs):
        pass

    def _map_to_dal(self, item: ServiceDOM):
        return ServiceDAL(item).db_serializer()

    def _map_to_dom(self, item: ServiceDAL):
        return ServiceDAL(item).db_deserializer()

    def _map_filter(self, filter: Optional[dict]):
        return {} if filter is None else filter
