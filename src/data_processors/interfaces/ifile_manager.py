from abc import ABC, abstractmethod

class IFileManager(ABC):

    @abstractmethod
    def read(file_name):
        pass

    @abstractmethod
    def write(file_name, data):
        pass


