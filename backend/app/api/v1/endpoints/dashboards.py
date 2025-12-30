from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.dashboard import DashboardCreate, DashboardResponse
from app.services.dashboard_service import DashboardService

router = APIRouter()

@router.get("/", response_model=List[DashboardResponse])
async def get_dashboards(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    return service.get_dashboards(skip=skip, limit=limit)

@router.post("/", response_model=DashboardResponse)
async def create_dashboard(
    dashboard: DashboardCreate,
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    return service.create_dashboard(dashboard)

@router.get("/{dashboard_id}", response_model=DashboardResponse)
async def get_dashboard(
    dashboard_id: int,
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    dashboard = service.get_dashboard_by_id(dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    return dashboard

