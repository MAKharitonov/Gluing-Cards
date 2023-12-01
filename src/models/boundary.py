from typing import List, Optional
from src.models.zone import Zone
from pydantic import BaseModel, Field, conint

class Boundary(BaseModel):
    x: List[int]
    y: List[int]


