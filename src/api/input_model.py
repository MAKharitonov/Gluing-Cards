import pydantic_numpy.typing as pnd
from src.models.piecewise_linear_function import PiecewiseLinearFunction
from src.models.сhannel_model import ChannelModel
from src.task.task import Task
from typing import List, Optional
from src.models.zone import Zone

from pydantic import BaseModel, Field
from pydantic_numpy.model import NumpyModel


class InputModel(BaseModel):
    """
    Входные данные для задачи склейки русел
    """
    output_file_name: str = Field(alias="outputFileName")
    path_to_map_case: str = Field(alias="pathToMapCase")
    days: int
    zones: List[Zone]
    up_bound_volga_zone: PiecewiseLinearFunction = Field(alias="upBoundVolgaZone")
    low_bound_akhtuba_zone: PiecewiseLinearFunction = Field(alias="lowBoundAkhtubaZone")
    volga_left_coast: PiecewiseLinearFunction = Field(alias="volgaLeftCoast")
    volga_right_coast: PiecewiseLinearFunction = Field(alias="volgaRightCoast")
    akhtuba_left_coast: PiecewiseLinearFunction = Field(alias="akhtubaLeftCoast")
    akhtuba_right_coast: PiecewiseLinearFunction = Field(alias="akhtubaRightCoast")
    cell_size: int = Field(alias="cellSize")







