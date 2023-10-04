from src.data_processors.interfaces.ifile_manager import IFileManager
import numpy as np
import struct

class FileManager(IFileManager):

    @staticmethod
    def read(file_name):
        try:
            f = open(file_name, "rb")
            c = f.read(4).decode("utf-8")
            # print(C)
            n_x = int.from_bytes(f.read(2), "little")  # кол-во ячеек по Х
            # print(N_x)
            n_y = int.from_bytes(f.read(2), "little")  # кол-во ячеек по Y
            # print(N_y)
            region_bound = struct.unpack('6d', f.read(6 * 8))
            # print(P)
            dem = np.zeros((n_x, n_y))
            # далее читаем матрицу построчно и записываем в Matr
            for i in range(n_x):
                for j in range(n_y):
                    temp = struct.unpack('f', f.read(4))
                    dem[i][j] = temp[0]
        except IOError:
            print("An IOError has occurred!")
        finally:
            f.close()
        return dem, region_bound, n_x, n_y

    @staticmethod
    def write(file_name, id_surfer, n_x, n_y, region_bound,  dem):
        try:
            f = open(file_name, "wb")
            f.write(id_surfer.encode("utf-8"))
            f.write(struct.pack('h', n_x))
            f.write(struct.pack('h', n_y))
            f.write(struct.pack('6d',
                                region_bound[0], region_bound[1], region_bound[2], region_bound[3],
                                np.min(dem), np.max(dem)))
            for i in range(n_x):
                for j in range(n_y):
                    f.write(struct.pack('f', dem[i][j]))
        except IOError:
            print("An IOError has occurred!")
        finally:
            f.close()
