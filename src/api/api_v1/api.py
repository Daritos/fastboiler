from fastapi import APIRouter

from .endpoints.example import router as triage_router


router = APIRouter()
router.include_router(triage_router)
