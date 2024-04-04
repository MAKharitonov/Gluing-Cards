from src.api.zone import Zone
from typing import List
from pydantic import BaseModel, Field



class Task(BaseModel):
    zones: List[Zone] = Field(alias="zones")
    days: int = Field(alias="days")
    output_file_name: str = Field(alias="outputFileName")


