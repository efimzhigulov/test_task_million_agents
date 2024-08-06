from typing import Annotated, List

import asyncio
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from app.logic.datastructure import FileAdd

router = APIRouter()


@router.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):

    await FileAdd.create(file)

    return {"message": "File uploaded successfully"}


@router.post("/stream_upload/")
async def stream_upload_file(file: bytes = File()):

    await FileAdd.create_stream(file)

    return {"message": "File uploaded successfully"}


