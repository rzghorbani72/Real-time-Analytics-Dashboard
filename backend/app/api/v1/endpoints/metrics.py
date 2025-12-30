from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.metric import MetricCreate, MetricResponse
from app.services.metric_service import MetricService

router = APIRouter()

@router.get("/", response_model=List[MetricResponse])
async def get_metrics(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    service = MetricService(db)
    return service.get_metrics(skip=skip, limit=limit)

@router.post("/", response_model=MetricResponse)
async def create_metric(
    metric: MetricCreate,
    db: Session = Depends(get_db)
):
    service = MetricService(db)
    return service.create_metric(metric)

@router.get("/{metric_id}", response_model=MetricResponse)
async def get_metric(
    metric_id: int,
    db: Session = Depends(get_db)
):
    service = MetricService(db)
    metric = service.get_metric_by_id(metric_id)
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric

