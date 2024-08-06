from fastapi import APIRouter
from app.api.routes.v1.endpoints import router as endoint_router

router = APIRouter()
router.include_router(endoint_router, tags=["endpoints1"], prefix="/v1")