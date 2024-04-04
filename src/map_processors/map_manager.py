from src.data_processors.file_manager import FileManager
from src.map_processors.flood_check import FloodCheck
from src.app.logger import logger

import numpy as np


class MapManager:
    def __init__(self, task, input_data, digital_relief_model):
        self.task = task
        self.drm = digital_relief_model
        self.data = input_data


    def __loading_maps(self):
        """
        Загрузка необходимых карт из
        базового корпуса карт затопления
        :return: матрица высот [номер зоны][x][y]
        """
        number_zones = len(self.task.zones.zone_length)
        q_array = self.task.zones.zone_hydrograph
        n_x = self.drm.amount_x
        n_y = self.drm.amount_y
        dem = np.zeros((number_zones, n_x, n_y))
        file_manager = FileManager()

        for zone in range(number_zones):
            file_name = self.__build_file_name(q_array[zone])
            digital_relief_model = file_manager.read(file_name)
            dem[zone][::][::] = digital_relief_model.dem

        return dem

    def __build_file_name(self, zone_hydrograph):
        """
        Потроение имени файла с рельефом,
        который нужно загрузить из базового корпуса карт затопления
        :param q: гидрограф
        :return: имя файла
        """
        h = str(int(zone_hydrograph / 10))
        name = (self.data.path_to_map_case + "расчет_2023_манинг_q"
                + h + "_30day/H_   " + str(self.task.days) + ".grd")

        return name

    def __get_set_closest_points(self, piecewise_linear_function):
        #PointVolgaChannel
        pass

    def __select_zone(self, x_length, y_length, x_zon, y_zon, H, x, y):
        if self.calc_line_equation(x_length[0], y_length[0], x_zon[0], y_zon[0], x) < y:
            return H[0][y][x]
        if self.calc_line_equation(x_length[len(x_length) - 1], y_length[len(x_length) - 1], x_zon[len(x_length) - 1],
                        y_zon[len(x_length) - 1], x) > y:
            return H[len(x_length)][y][x]
        for point in range(1, len(x_length)):
            if self.calc_line_equation(x_length[point], y_length[point], x_zon[point], y_zon[point], x) <= y <= self.calc_line_equation(
                    x_length[point - 1], y_length[point - 1], x_zon[point - 1], y_zon[point - 1], x):
                return H[point][y][x]



    def calc_line_equation(x_a, y_a, x_b, y_b, x):
        """
        Уравнение прямой проходящей через точки (x_a, y_a) и (x_b, y_b)
        """
        try:
            line_equation = ((y_b - y_a) / (x_b - x_a)) * (x - x_a) + y_a
            logger.debug(f"Уравнение прямой проходящей через точки ({x_a},{y_a}) и ({x_b},{y_b}) успешно составлено.")
        except ZeroDivisionError:
            logger.error(f"Деление на ноль!!!")

        return line_equation

    def gluing_flood_maps(self, x, y):
        n_x = self.drm.amount_x
        n_y = self.drm.amount_y
        bound_volga = self.task.up_bound_volga_zone
        bound_akhtuba = self.task.low_bound_akhtuba_zone
        check = FloodCheck(bound_volga, bound_akhtuba)

        for y in range(n_y):
            for x in range(n_x):
                if check.flooding_from_akhtuba(x, y):
                    print("flooding_from_akhtuba")
                elif check.flooding_from_volga(x, y):
                    print("flooding_from_volga")
                else:
                    print("flooding_from_akhtuba_and_volga")

