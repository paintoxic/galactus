from typing import Optional
from pydantic import BaseModel


class SchemesAPI(BaseModel):
    id: Optional[str]
    description: str
    metadata: dict
    name: str
