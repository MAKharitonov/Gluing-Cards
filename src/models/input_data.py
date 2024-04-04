from src.models.сhannel_model import ChannelModel


class InputData:

    def __init__(self, input_data_model):
        self.up_bound_volga_zone = input_data_model.up_bound_volga_zone
        self.low_bound_akhtuba_zone = input_data_model.low_bound_akhtuba_zone
        self.volga_channel = ChannelModel(input_data_model.volga_left_coast, input_data_model.volga_right_coast)
        self.akhtuba_channel = ChannelModel(input_data_model.akhtuba_left_coast, input_data_model.akhtuba_right_coast)
        self.cell_size = input_data_model.cell_size

