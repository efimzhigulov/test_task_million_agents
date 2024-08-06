from pydantic.v1 import BaseModel
from sqlalchemy.orm import as_declarative
from sqlalchemy.orm.decl_api import registry

mapper_registry = registry()
metadata = mapper_registry.metadata


@as_declarative(metadata=metadata)
class Base:
    pass
class BaseORM(Base):
    __abstract__ = True


def get_metadata():
    """Import all project tables"""
    from app.db.tables.file import FileORM  # noqa

    return mapper_registry.metadata