from core.endpoints import router as core_router
from fastapi import APIRouter

router = APIRouter()


router.include_router(core_router, tags=["Core"])

