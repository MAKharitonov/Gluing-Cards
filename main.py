from src.data_processors.file_manager import FileManager
from src.api.input_model import InputModel
from src.task.task import Task
import json

file_manager = FileManager()
file_name = "C:/Users/mikhail/Dropbox/test/H_9.grd"
drm = file_manager.read(file_name)

print(drm.region_bound)

with open("data/test1.json", "r", encoding='utf-8') as json_input:
    request = json.load(json_input)
print(request)

data_input = InputModel(**request)

task = Task(data_input)

t = task.volga_channel.left_coast

print(t)




