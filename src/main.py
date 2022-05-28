import aioredis
import os

from fastapi import FastAPI

from fastapi_limiter import FastAPILimiter

from api.api_v1.api import router as api_router
from api.core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod"
)

@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url(
        os.environ.get("REDIS_LIMITER_POOL", "redis://localhost:6379"), encoding="utf-8", decode_responses=True
    )
    #redis = await aioredis.create_redis_pool(os.environ.get("REDIS_LIMITER_POOL", "redis://localhost:6379"))
    await FastAPILimiter.init(redis)

app.include_router(api_router, prefix=API_V1_STR)
