from fastapi import APIRouter

from handlers import healthcheck_router

own_router = APIRouter()

own_router.include_router(healthcheck_router, tags=['Health Check'])
