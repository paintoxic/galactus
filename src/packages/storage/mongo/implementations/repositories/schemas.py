from typing import Optional
from domain.schemes.models.scheme_dom import SchemesDOM
from packages.storage.mongo.implementations.models.schemes_dal import SchemesDAL
from packages.storage.repository.base import BaseRepository
from pymongo.database import Database

_COLLECTION_NAME = 'schemes'


class SchemasMongoImplementation(BaseRepository):
    def __init__(self, database: Database) -> None:
        self._collection = database.get_collection(_COLLECTION_NAME)

    def get_by_id(self, id: str, **kwargs):
        entity = self._map_to_dom(self._collection.find_one({"_id": id}))
        return entity

    def get_and_count(self, filter: Optional[dict], **kwargs):
        rows = self._collection.find(self._map_filter(filter))
        response = [self._map_to_dom(item) for item in rows]
        count = self._collection.count_documents(self._map_filter(filter))
        return (response, count)

    def create(self, item, **kwargs):
        inserted = self._collection.insert_one(self._map_to_dal(item))
        return str(inserted.inserted_id)

    def update(self, id: str, item, **kwargs):
        pass

    def delete(self, id: str, **kwargs):
        pass

    def _map_to_dal(self, item: SchemesDOM):
        return SchemesDAL(item).db_serializer()

    def _map_to_dom(self, item: SchemesDAL):
        return SchemesDAL(item).db_deserializer()

    def _map_filter(self, filter: Optional[dict]):
        return {} if filter is None else filter
