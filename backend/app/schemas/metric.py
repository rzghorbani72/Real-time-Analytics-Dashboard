from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MetricBase(BaseModel):
    name: str
    value: float
    source: Optional[str] = None

class MetricCreate(MetricBase):
    pass

class MetricResponse(MetricBase):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True

