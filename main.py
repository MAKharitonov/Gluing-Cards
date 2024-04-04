from src.data_processors.file_manager import FileManager
from src.api.input_task_model import InputTaskModel
from src.api.input_data_model import InputDataModel
from src.models.input_data import InputData
import json


file_manager = FileManager()
file_name = "E:/Dropbox/test/H_9.grd"
drm = file_manager.read(file_name)


print(drm.region_bound)

with open("data/data.json", "r", encoding='utf-8') as json_input:
    data = json.load(json_input)
print(data)

data_model = InputDataModel(**data)

input_data = InputData(data_model)
t = input_data.volga_channel.left_coast

print(t)


with open("data/testTasks.json", "r", encoding='utf-8') as json_input:
    request = json.load(json_input)
print(request)

data_model = InputTaskModel(**request)

