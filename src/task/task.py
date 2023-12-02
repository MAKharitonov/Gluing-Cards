from src.models.piecewise_linear_function import PiecewiseLinearFunction
from src.models.zone import Zone
from src.models.сhannel_model import ChannelModel


#from src.api.input_data import InputModel


class Task:

    def __init__(self, input_model):
        self.output_file_name = input_model.output_file_name
        self.path_to_map_case = input_model.path_to_map_case
        self.days = input_model.days
        self.zones = input_model.zones
        self.up_bound_volga_zone = input_model.up_bound_volga_zone
        self.low_bound_akhtuba_zone = input_model.low_bound_akhtuba_zone
        self.volga_channel = ChannelModel(input_model.volga_left_coast, input_model.volga_right_coast)
        self.akhtuba_channel = ChannelModel(input_model.akhtuba_left_coast, input_model.akhtuba_right_coast)
        self.cell_size = input_model.cell_size


