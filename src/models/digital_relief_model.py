
class DigitalReliefModel:
    """
    Цифровая модель рельефа
    """

    def __init__(self, amount_x, amount_y, dem, region_bound, id_surfer="DSBB"):
        self._amount_x = amount_x
        self._amount_y = amount_y
        self._dem = dem
        self._region_bound = region_bound
        self._id_surfer = id_surfer


    @property
    def id_surfer(self):
        return self._id_surfer

    @id_surfer.setter
    def id_surfer(self):
        return self._id_surfer

    @property
    def amount_x(self):
        return self._amount_x

    @amount_x.setter
    def amount_x(self, amount_x):
        self._amount_x = amount_x

    @property
    def amount_y(self):
        return self._amount_y

    @amount_y.setter
    def amount_y(self, amount_y):
        self._amount_y = amount_y

    @property
    def dem(self):
        return self._dem

    @dem.setter
    def dem(self, dem):
        self._dem = dem

    @property
    def region_bound(self):
        return self._region_bound

    @region_bound.setter
    def region_bound(self, region_bound):
        self._region_bound = region_bound


