from src.models.piecewise_linear_function import PiecewiseLinearFunction
from src.models.zone import Zone
from src.models.сhannel_model import ChannelModel


#from src.api.input_data import InputModel


class Task:

    def __init__(self, im):
        self.output_file_name = im.output_file_name
        self.days = im.days
        self.zones = im.zones
        self.up_bound_volga_zone = im.up_bound_volga_zone
        self.low_bound_akhtuba_zone = im.low_bound_akhtuba_zone
        self.volga_channel = ChannelModel(im.volga_left_coast, im.volga_right_coast)
        self.cell_size = im.cell_size


