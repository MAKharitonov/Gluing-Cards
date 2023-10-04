from src.data_processors.interfaces.ifile_manager import IFileManager
from src.data_processors.file_manager import FileManager

file_manager = FileManager()

file_name = "/home/mikhail/Dropbox/test/relief_2403.grd"
file_name1 = "/home/mikhail/Dropbox/test/relief_410.grd"


(dem, region_bound, amount_x, amount_y) = file_manager.read(file_name)

print(region_bound)

file_manager.write(file_name, dem, region_bound, amount_x, amount_y)



