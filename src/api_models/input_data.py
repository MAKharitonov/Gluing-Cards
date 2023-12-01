import pydantic_numpy.typing as pnd
from src.models.boundary import Boundary
from src.task.task import Task
from typing import List, Optional
from src.models.zone import Zone

from pydantic import BaseModel, Field
from pydantic_numpy.model import NumpyModel

class InputModel(BaseModel):
    output_file_name: str = Field(alias="outputFileName")
    days: int
    zones: List[Zone]
    up_bound_volga_zone: Boundary = Field(alias="upBoundVolgaZone")
    low_bound_akhtuba_zone: Boundary = Field(alias="lowBoundAkhtubaZone")
    volga_channels: Boundary = Field(alias="volgaChannels")
    akhtuba_channels: Boundary = Field(alias="akhtubaChannels")







