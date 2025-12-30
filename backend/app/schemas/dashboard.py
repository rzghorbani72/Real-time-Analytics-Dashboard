from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class DashboardBase(BaseModel):
    name: str
    description: Optional[str] = None
    config: Dict[str, Any] = {}

class DashboardCreate(DashboardBase):
    pass

class DashboardResponse(DashboardBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

