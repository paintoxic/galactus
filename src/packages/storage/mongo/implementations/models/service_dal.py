
from collections.abc import Mapping


class ServiceDAL(object):
    id: str
    description: str
    name: str
    main_scheme: str
    backends: list

    def __init__(self, item):
        if isinstance(item, Mapping) is True:
            self._from_dict(item)
        else:
            self._from_object(item)

    def _from_dict(self, item: dict):
        self._id = item["_id"]
        self.description = item["description"]
        self.name = item["name"]
        self.main_scheme = item["main_scheme"]
        self.backends = item["backends"]

    def _from_object(self, item):
        self.id = item.id
        self.description = item.description
        self.name = item.name
        self.main_scheme = item.main_scheme
        self.backends = item.backends

    def db_serializer(self):
        return {
            "_id": self.id,
            "description": self.description,
            "name": self.name,
            "main_scheme": self.main_scheme,
            "backends": self.backends,
        }

    def db_deserializer(self):
        return {
            "id": self._id,
            "description": self.description,
            "name": self.name,
            "main_scheme": self.main_scheme,
            "backends": self.backends,
        }
