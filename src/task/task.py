from src.models.boundary import Boundary
from src.models.zone import Zone
#from src.api_models.input_data import InputModel


class Task:

    def __init__(self, InputModel):
        self.output_file_name = InputModel.output_file_name
        self.days = InputModel.days
        self.zones = InputModel.zones
        self.up_bound_volga_zone = InputModel.up_bound_volga_zone
        self.low_bound_akhtuba_zone = InputModel.low_bound_akhtuba_zone
        self.volga_channels = InputModel.volga_channels
        self.akhtuba_channels = InputModel.akhtuba_channels


