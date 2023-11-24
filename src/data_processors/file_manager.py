from src.models.digital_relief_model import DigitalReliefModel
import numpy as np
import struct

class FileManager:
    """
    Класс для работы с файлами  *.grd
    """

    @staticmethod
    def read(file_name):
        """
        Считывание *.grd файла
        :param file_name: имя файла
        :return: DigitalReliefModel
        """
        try:
            f = open(file_name, "rb")
            id_surfer = f.read(4).decode("utf-8")
            amount_x = int.from_bytes(f.read(2), "little")  # кол-во ячеек по Х
            amount_y = int.from_bytes(f.read(2), "little")  # кол-во ячеек по Y
            region_bound = struct.unpack('6d', f.read(6*8))

            dem = np.zeros((amount_x, amount_y))
            for x in range(amount_x):
                for y in range(amount_y):
                    temp = struct.unpack('f', f.read(4))
                    dem[x][y] = temp[0]
        except IOError:
            print("An IOError has occurred!")
        finally:
            f.close()

        return DigitalReliefModel(amount_x, amount_y, dem, region_bound, id_surfer)#dem, region_bound[:4], amount_x, amount_y

    @staticmethod
    def write(file_name, digital_relief_model):
        """
        Запись *.grd файла
        :param file_name: имя файла
        :param digital_relief_model:
        :return:
        """
        try:
            f = open(file_name, "wb")
            f.write(digital_relief_model.id_surfer.encode("utf-8"))
            f.write(struct.pack('h', digital_relief_model.amount_x))
            f.write(struct.pack('h', digital_relief_model.amount_yamount_y))
            f.write(struct.pack('6d',
                                digital_relief_model.region_bound[0],
                                digital_relief_model.region_bound[1],
                                digital_relief_model.region_bound[2],
                                digital_relief_model.region_bound[3],
                                np.min(digital_relief_model.dem),
                                np.max(digital_relief_model.dem)))
            for x in range(digital_relief_model.amount_x):
                for y in range(digital_relief_model.amount_y):
                    f.write(struct.pack('f', digital_relief_model.dem[x][y]))
        except IOError:
            print("An IOError has occurred!")
        finally:
            f.close()
