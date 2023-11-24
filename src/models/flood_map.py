from src.data_processors.file_manager import FileManager
from src.models.digital_relief_model import DigitalReliefModel

import numpy as np

class FloodMap:


    def LoadingMaps(self, q_array, number_zones, day, path, n_x, n_y):
        dem = np.zeros((number_zones, n_x, n_y))
        file_manager = FileManager()
        for zone in range(number_zones):
            file_name = self.build_file_name(path, q_array[zone], day)
            digital_relief_model = file_manager.read(file_name)
            dem[zone][::][::] = digital_relief_model.dem
        return dem

    @staticmethod
    def build_file_name(path, q, day):
        q_str = str(int(q / 10))
        return path + "расчет_2023_манинг_q" + q_str + "_30day/H_   " + str(day) + ".grd"