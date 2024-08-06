from pydantic.v1 import BaseSettings
from starlette.config import Config



config = Config(".env")

class APPSettings(BaseSettings):
    PROJECT_NAME: str = config("PROJECT_NAME", default='Test_task')
    DATABASE_URL: str = config("DATABASE_URL", default='postgresql+asyncpg://postgres:2009@localhost:5432/postgres')
    DEBUG: bool = config("DEBUG",default=True)

    S3_ACCESS_KEY: str = config('S3_ACCESS_KEY',default='')
    S3_SECRET_KEY: str = config('S3_SECRET_KEY',default='')
    S3_ENDPOINT_URL: str = config('S3_ENDPOINT_URL',default='')
    S3_BUCKET_NAME: str = config('S3_BUCKET_NAME',default='')
    class Config:
        env_file = ".env"

def get_app_settings() -> APPSettings:
    return APPSettings()