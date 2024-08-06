from typing import Optional
import uuid as uuid_pkg
from pydantic import Field
from pydantic.v1 import BaseModel
from sqlalchemy import UUID, String


class File(BaseModel):
    uuid: uuid_pkg.UUID = Field()
    file_size: int = Field()
    original_name: str = Field()
    file_extension: str = Field()
    file_format: str = Field()