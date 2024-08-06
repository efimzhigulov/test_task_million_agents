import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from app.db.tables.base import BaseORM

class FileORM(BaseORM):
    __tablename__ = "file"

    uuid = sa.Column(UUID(as_uuid=True), primary_key=True)
    file_size = sa.Column('file_size',sa.BIGINT)
    original_name = sa.Column('original_name',sa.String(255))
    file_extension = sa.Column('file_extension',sa.String(8))
    file_format = sa.Column('file_format',sa.String(5))