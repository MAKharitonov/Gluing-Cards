from typing import List
from pydantic import BaseModel
import numpy as np
import sys

class PiecewiseLinearFunction(BaseModel):
    """
    Кусочно-линейная модель
    """
    x: List[int]
    y: List[int]


    def get_closest_point(self, length_zone):
        """
        Получить координаты ближайщей к границе зоны точки
        :param length_zone: длина зоны
        :return: x,y
        """
        min_length = sys.maxsize
        length_channel = 0
        number = -1
        for i in range(len(self.x) - 1):
            length = np.linalg.norm(
                np.array([self.x[i + 1], self.y[i + 1]]) - np.array([self.x[i], self.y[i]]))
            length_channel = length_channel + self.cell_size * length
            if np.abs(length_zone - length_channel) < min_length:
                min_length = np.abs(length_zone - length_channel)
                number = i + 1
        if number == -1:
            return "Ошибка модели! PiecewiseLinearFunction.get_closest_point не найдена точка"

        return self.x[number], self.y[number]



