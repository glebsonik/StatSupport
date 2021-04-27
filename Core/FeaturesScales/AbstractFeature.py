class AbstractFeature:

    _name = None
    _aggregated_data = {}
    _scale = None

    def __init__(self, feature_name, aggregated_data):
        self._name = feature_name
        self._aggregated_data = aggregated_data

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
