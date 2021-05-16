import copy
from Core.Service.DataAggregator import DataAggregator
class AbstractFeature:

    _name = None
    _aggregated_data = {}
    _scale = None

    def __init__(self, feature_name, data):
        self._name = feature_name
        self.data = copy.deepcopy(data)
        self._aggregated_data = DataAggregator.aggregate_list(data)

    def get_stat_info(self):
        raise NotImplementedError("Abstract class has no methods implementation")

    @property
    def scale(self):
        return self._scale

    @property
    def name(self):
        return self._name

    @property
    def aggregated_data(self):
        return self._aggregated_data
