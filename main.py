from src.data_processors.file_manager import FileManager
from src.api_models.input_data import InputModel
from src.task.task import Task

import json

file_manager = FileManager()

file_name = "/home/mikhail/Dropbox/test/H_9.grd"

drm = file_manager.read(file_name)

#dem, region_bound, amount_x, amount_y = file_manager.read(file_name)
print(drm.region_bound)

with open("data/test1.json", "r", encoding='utf-8') as json_in:
    req = json.load(json_in)
print(req)


task = InputModel(**req)

#file_manager.write(file_name, drm)



