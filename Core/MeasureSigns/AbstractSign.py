class AbstractMeasureSign:

    _name = None
    _aggregated_data = {}
    _measure = None

    def __init__(self, sign_name, aggregated_data):
        self._name = sign_name
        self._aggregated_data = aggregated_data

    def get_stat_info(self):
        raise NotImplementedError("Abstract class has no methods implementation")

    @property
    def measure(self):
        return self._measure

    @property
    def name(self):
        return self._name

    @property
    def aggregated_data(self):
        return self._aggregated_data
