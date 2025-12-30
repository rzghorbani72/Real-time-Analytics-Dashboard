from sqlalchemy.orm import Session
from typing import List
from app.models.metric import Metric
from app.schemas.metric import MetricCreate

class MetricRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Metric]:
        return self.db.query(Metric).offset(skip).limit(limit).all()
    
    def get_by_id(self, metric_id: int) -> Metric:
        return self.db.query(Metric).filter(Metric.id == metric_id).first()
    
    def create(self, metric: MetricCreate) -> Metric:
        db_metric = Metric(**metric.model_dump())
        self.db.add(db_metric)
        self.db.commit()
        self.db.refresh(db_metric)
        return db_metric

