from abc import ABC, abstractmethod

class IFileManager(ABC):

    @staticmethod
    @abstractmethod
    def read(file_name):
        pass

    @staticmethod
    @abstractmethod
    def write(file_name, dem, region_bound, n_x, n_y):
        pass


