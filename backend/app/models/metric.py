from sqlalchemy import Column, Integer, String, Float, DateTime, Index
from sqlalchemy.sql import func
from app.core.database import Base

class Metric(Base):
    __tablename__ = "metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)
    source = Column(String, nullable=True, index=True)
    
    __table_args__ = (
        Index('idx_metric_timestamp_source', 'timestamp', 'source'),
        Index('idx_metric_name_timestamp', 'name', 'timestamp'),
    )

