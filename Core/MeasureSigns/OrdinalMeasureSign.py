from .AbstractSign import AbstractMeasureSign
from .SelfStatisticCalculators.OrdinalCalculator import OrdinalCalculator


class OrdinalMeasureSign(AbstractMeasureSign):

    ordered_data = []
    _measure = 'Ordinal'

    def __init__(self, name, aggregated_data, ranks):
        super(OrdinalMeasureSign, self).__init__(name, aggregated_data)
        allowed_names = aggregated_data.keys()
        if len(ranks) != len(allowed_names):
            raise IndexError(f'Incorrect keys count in ranks expected: {len(allowed_names)} got: {len(ranks)}')
        for rank_name in ranks:
            if rank_name not in allowed_names:
                raise KeyError(f'No such sign name {rank_name} found in {allowed_names}')
            self.ordered_data.append(rank_name)

    def get_stat_info(self):
        OrdinalCalculator().calc_mode(self._aggregated_data)
        # OrdinalCalculator().calc_median()
        # OrdinalCalculator().calc_max()
        # OrdinalCalculator().calc_min()
