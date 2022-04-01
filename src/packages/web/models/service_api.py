from typing import Optional
from pydantic import BaseModel


class ServiceAPI(BaseModel):
    id: Optional[str]
    description: str
    name: str
    main_scheme: str
    backends: list
