from io import BytesIO
from httpx import AsyncClient
import pytest
from PIL import Image
from main import app


@pytest.fixture(scope='session')
async def async_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


def create_dummy_image(file_type: str = "jpeg"):
    image_buffer = BytesIO()
    image = Image.new("RGB", (100, 100))
    image.save(image_buffer, file_type)
    image_buffer.name = "dummy." + file_type
    image_buffer.seek(0)
    return image_buffer

def create_test_file(size_in_bytes: int, filename: str = "hello.jpg"):
    file_buffer = BytesIO()
    file_buffer.write(b"0" * size_in_bytes)
    file_buffer.name = filename
    file_buffer.seek(0)
    return file_buffer
