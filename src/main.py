from fastapi import FastAPI

from api.api_v1.api import router as api_router
from api.core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod"
)

app.include_router(api_router, prefix=API_V1_STR)
