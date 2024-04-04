from src.models.piecewise_linear_function import PiecewiseLinearFunction

from pydantic import BaseModel, Field


class InputDataModel(BaseModel):
    """
    Модель входных данных ( линейное приближение русла рек, зоны затопление из Волги и Ахтубы)
    """
    up_bound_volga_zone: PiecewiseLinearFunction = Field(alias="upBoundVolgaZone")
    low_bound_akhtuba_zone: PiecewiseLinearFunction = Field(alias="lowBoundAkhtubaZone")
    volga_left_coast: PiecewiseLinearFunction = Field(alias="volgaLeftCoast")
    volga_right_coast: PiecewiseLinearFunction = Field(alias="volgaRightCoast")
    akhtuba_left_coast: PiecewiseLinearFunction = Field(alias="akhtubaLeftCoast")
    akhtuba_right_coast: PiecewiseLinearFunction = Field(alias="akhtubaRightCoast")
    cell_size: int = Field(alias="cellSize")
    path_to_map_case: str = Field(alias="pathToMapCase")