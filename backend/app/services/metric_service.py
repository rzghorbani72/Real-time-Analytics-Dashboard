from sqlalchemy.orm import Session
from typing import List
from app.models.metric import Metric
from app.schemas.metric import MetricCreate
from app.repositories.metric_repository import MetricRepository

class MetricService:
    def __init__(self, db: Session):
        self.repository = MetricRepository(db)
    
    def get_metrics(self, skip: int = 0, limit: int = 100) -> List[Metric]:
        return self.repository.get_all(skip=skip, limit=limit)
    
    def get_metric_by_id(self, metric_id: int) -> Metric:
        return self.repository.get_by_id(metric_id)
    
    def create_metric(self, metric: MetricCreate) -> Metric:
        return self.repository.create(metric)

