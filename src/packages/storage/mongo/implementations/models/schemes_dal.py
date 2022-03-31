
from collections.abc import Mapping


class SchemesDAL(object):
    id: str
    description: str
    metadata: dict
    name: dict

    def __init__(self, item):
        if isinstance(item, Mapping) is True:
            self._from_dict(item)
        else:
            self._from_object(item)

    def _from_dict(self, item: dict):
        self._id = item["_id"]
        self.description = item["description"]
        self.metadata = item["metadata"]
        self.name = item["name"]

    def _from_object(self, item):
        self.id = item.id
        self.description = item.description
        self.metadata = item.metadata
        self.name = item.name

    def db_serializer(self):
        return {
            "_id": self.id,
            "description": self.description,
            "metadata": self.metadata,
            "name": self.name,
        }

    def db_deserializer(self):
        return {
            "id": self._id,
            "description": self.description,
            "metadata": self.metadata,
            "name": self.name,
        }
