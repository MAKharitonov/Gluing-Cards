from src.task.task import Task
from src.data_processors.file_manager import FileManager
from src.map_processors.flood_check import FloodCheck
import numpy as np



class MapManager:
    def __init__(self, task, digital_relief_model):
        self.task = task
        self.drm = digital_relief_model

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
        name = (self.task.path_to_map_case + "расчет_2023_манинг_q"
                + h + "_30day/H_   " + str(self.task.days) + ".grd")

        return name

    def __get_set_closest_points(self, piecewise_linear_function):
        #PointVolgaChannel
        pass



    def __select_zone(self):
        #SelectionZone
        pass

    @staticmethod
    def __calc_line_equation(x_a, y_a, x_b, y_b, x):
        """
        Уравнение прямой проходящей через точки (x_a, y_a) и (x_b, y_b)
        """
        return ((y_b - y_a) / (x_b - x_a)) * (x - x_a) + y_a


    def gluing_flood_maps(self,x,y):
        n_x = self.drm.amount_x
        n_y = self.drm.amount_y
        bound_volga = self.task.up_bound_volga_zone
        bound_akhtuba = self.task.low_bound_akhtuba_zone
        check = FloodCheck(bound_volga, bound_akhtuba)

        #for y in range(n_y):
            #for x in range(n_x):
                #if check.flooding_from_akhtuba(x,y):
                    #print("flooding_from_akhtuba")
                #elif check.flooding_from_volga(x,y):
                    #print("flooding_from_volga")
                #else:
                    #print("flooding_from_akhtuba_and_volga")

        return check.flooding_from_volga(x, y)








