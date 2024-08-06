import os
import uuid
from typing import Dict, Union
from app.db import FileORM
from app.db.setup import async_session
from app.logic.s3 import upload_file_to_s3
from app.schemas.file import File


class FileAdd:
    @classmethod
    async def create(cls, file):
            with open(f"uploaded_files/{file.filename}", "wb") as f:
                # Загрузка файла на диск
                try:
                    await cls.upload_file(f, file)
                except Exception as e:
                    return (f'ошибка ({e}) загрузки файла {file.filename}')
                else:
                    await cls.handle(f)

    @classmethod
    async def create_stream(cls, file):
            with open(f"streamed_files/file.bin", "wb") as f:
                # Загрузка файла на диск через стрим
                try:
                    await cls.stream_upload_file(f,file)
                except Exception as e:
                    return (f'ошибка ({e}) загрузки файла')
                else:
                    await cls.handle(f)

    @classmethod
    async def handle(cls, f) -> None | str:
        # Получение метаданных файла
        metadata = await cls.get_metadata(f)
        if not metadata:
            print('Ошибка получения метаданных файла')
            return None
        # Валидация
        validated_metadata = await cls.validate_file(metadata)
        if not validated_metadata:
            print('Ошибка валидации метаданных файла')
            return None
        # Сохранение метаданных файла в базу
        await cls.save_metadata_to_db(validated_metadata)
        # Отправка файла в S3
        try:
            await upload_file_to_s3(metadata["original_name"])
        except ValueError:
            print('Добавьте креды в .env для подключения к хранилищу')
        return None

    @classmethod
    async def stream_upload_file(cls, f, file) -> None:
        f.write(file)
        return None

    @classmethod
    async def upload_file(cls, f, file) -> None:
        new_file = f.write(file.file.read())
        return new_file

    @classmethod
    async def get_metadata(cls, f) -> Dict[str, Union[uuid, int, str]]:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()
        file_name = os.path.basename(f.name)
        file_extension = file_name.split('.')[-1]
        original_name = '.'.join(file_name.split('.')[:-1])
        image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
        video_extensions = ['avi', 'mp4', 'mkv', 'mov', 'wmv']
        audio_extensions = ['mp3', 'wav', 'flac', 'aac']
        bin_extension = ['bin']
        if file_extension in image_extensions:
            file_format = 'image'
        elif file_extension in video_extensions:
            file_format = 'video'
        elif file_extension in audio_extensions:
            file_format = 'audio'
        elif file_extension in bin_extension:
            file_format = 'bin'
        else:
            file_format = 'unknown'
        metadata = {"uuid": uuid.uuid4(), "file_size": file_size, "original_name": original_name, "file_extension": file_extension,
                    "file_format": file_format}

        return metadata

    @classmethod
    async def save_metadata_to_db(cls, metadata: File):
        async with async_session() as session:
            session.add(FileORM(**metadata.dict()))
            await session.commit()
            await session.close()

    @classmethod
    async def validate_file(cls, metadata: Dict[str, Union[uuid, int, str]]) -> File:
        validated_models = File(**metadata)
        return validated_models









