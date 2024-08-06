from contextlib import asynccontextmanager
from aiobotocore.session import get_session
from botocore.exceptions import ClientError
from app.core import config


class S3Client:
    def __init__(
            self,
            access_key: str,
            secret_key: str,
            endpoint_url: str,
            bucket_name: str,
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(
            self,
            file_name: str,
    ):
        try:
            async with self.get_client() as client:
                with open(f"uploaded_files/{file_name}", "rb") as f:
                    await client.put_object(
                        Bucket=self.bucket_name,
                        Key=file_name,
                        Body=f,
                    )
                print(f"Файл {file_name} загружен в {self.bucket_name}")
        except ClientError as e:
            print(f"Ошибка загрузки файла: {e}")


async def upload_file_to_s3(file_name):
    s3_client = S3Client(
        access_key=config.S3_ACCESS_KEY,
        secret_key=config.S3_SECRET_KEY,
        endpoint_url=config.S3_ENDPOINT_URL,
        bucket_name=config.S3_BUCKET_NAME,
    )
    await s3_client.upload_file(file_name)
