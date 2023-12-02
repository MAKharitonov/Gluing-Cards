from typing import List, Optional
from src.models.zone import Zone
from pydantic import BaseModel, Field, conint
import numpy as np
import sys

class PiecewiseLinearFunction(BaseModel):
    """
    Кусочно-линейная модель
    """
    x: List[int]
    y: List[int]

    def get_number_closest_point(self, length_zone):
        """
        Получить номер ближайщей к границе зоны точки
        :param length_zone: длина зоны
        :return: номер точки
        """
        cell_size = 50
        min_length = sys.maxsize
        length_channel = 0
        for i in range(len(self.x) - 1):
            length = np.linalg.norm(
                np.array([self.x[i + 1], self.y[i + 1]]) - np.array([self.x[i], self.y[i]]))
            length_channel = length_channel + cell_size * length
            if np.abs(length_zone - length_channel) < min_length:
                min_length = np.abs(length_zone - length_channel)
                number = i + 1
        return number



