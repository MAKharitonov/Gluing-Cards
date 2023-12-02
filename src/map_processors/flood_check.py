import numpy as np


class FloodCheck:
    def __init__(self, up_bound_volga_zone, low_bound_akhtuba_zone):
        self.volga_zone = up_bound_volga_zone
        self.akhtuba_zone = low_bound_akhtuba_zone

    def flooding_from_volga(self, x, y):
        """
        Проверка затапливается ли точка
        с координатами (x,y) из реки Волга.
        """
        if y <= np.max(self.volga_zone.y):
            return np.interp(x, self.volga_zone.x[::-1], self.volga_zone.y[::-1]) > y

    def flooding_from_akhtuba(self, x, y):
        """
        Проверка затапливается ли точка
        с координатами (x,y) из реки Ахтуба.
        """
        if y <= np.max(self.akhtuba_zone.y):
            return np.interp(x, self.akhtuba_zone.x[::-1], self.akhtuba_zone.y[::-1]) < y





