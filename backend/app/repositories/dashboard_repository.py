from sqlalchemy.orm import Session
from typing import List
from app.models.dashboard import Dashboard
from app.schemas.dashboard import DashboardCreate

class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Dashboard]:
        return self.db.query(Dashboard).offset(skip).limit(limit).all()
    
    def get_by_id(self, dashboard_id: int) -> Dashboard:
        return self.db.query(Dashboard).filter(Dashboard.id == dashboard_id).first()
    
    def create(self, dashboard: DashboardCreate) -> Dashboard:
        db_dashboard = Dashboard(**dashboard.model_dump())
        self.db.add(db_dashboard)
        self.db.commit()
        self.db.refresh(db_dashboard)
        return db_dashboard

