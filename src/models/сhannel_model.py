from typing import List, Optional
from src.models.piecewise_linear_function import PiecewiseLinearFunction
from pydantic import BaseModel, Field, conint
class ChannelModel:
    """
    Модель русла реки.
    """
    def __init__(self, left_coast, right_coast):
        self.left_coast = left_coast
        self.right_coast = right_coast

