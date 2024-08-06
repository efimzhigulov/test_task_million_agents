import pytest
from app.logic.datastructure import FileAdd
from tests.conftest import create_test_file, create_dummy_image


async def test_get_metadata():
    metadata = await FileAdd.get_metadata(create_dummy_image())
    assert metadata["file_size"] == 823
    assert metadata["original_name"] == 'dummy'
    assert metadata["file_extension"] == 'jpeg'
    assert metadata["file_format"] == 'image'



@pytest.mark.integration
@pytest.mark.asyncio
async def test_file_upload_success(async_client):
    response = await async_client.post("/v1/upload_file/", files={"file": create_test_file(1024 * 1)})
    assert response.status_code == 200
    assert response.json() == {"message": "File uploaded successfully"}



