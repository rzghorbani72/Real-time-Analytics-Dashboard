from sqlalchemy.orm import Session
from typing import List
from app.models.dashboard import Dashboard
from app.schemas.dashboard import DashboardCreate
from app.repositories.dashboard_repository import DashboardRepository

class DashboardService:
    def __init__(self, db: Session):
        self.repository = DashboardRepository(db)
    
    def get_dashboards(self, skip: int = 0, limit: int = 100) -> List[Dashboard]:
        return self.repository.get_all(skip=skip, limit=limit)
    
    def get_dashboard_by_id(self, dashboard_id: int) -> Dashboard:
        return self.repository.get_by_id(dashboard_id)
    
    def create_dashboard(self, dashboard: DashboardCreate) -> Dashboard:
        return self.repository.create(dashboard)

