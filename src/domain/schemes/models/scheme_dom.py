from typing import Optional

from fastapi import HTTPException

from packages.helpers import generate_uuid4, is_valid_uuid_4


class SchemesDOM(object):
    id: Optional[str]
    description: str
    metadata: dict
    name: str

    def __init__(self, item: dict):
        self._validate_id(item)
        self.description = item["description"]
        self.metadata = item["metadata"]
        self.name = item["name"]

    def _validate_id(self, item: dict):
        id = item["id"]
        if id is None:
            self.id = generate_uuid4()
        else:
            if is_valid_uuid_4(id) is True:
                self.id = id
            else:
                raise HTTPException(status_code=400, detail="Id isn't valid")
