from src.data_processors.file_manager import FileManager
from src.data_models.digital_relief_model import DigitalReliefModel

file_manager = FileManager()

file_name = "/home/mikhail/Dropbox/test/H_9.grd"

drm = file_manager.read(file_name)

#dem, region_bound, amount_x, amount_y = file_manager.read(file_name)
print(drm.region_bound)

#file_manager.write(file_name, drm)



