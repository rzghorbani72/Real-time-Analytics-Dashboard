from fastapi import APIRouter
from app.api.v1.endpoints import metrics, dashboards

api_router = APIRouter()

api_router.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
api_router.include_router(dashboards.router, prefix="/dashboards", tags=["dashboards"])

