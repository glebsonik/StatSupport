import copy
import matplotlib.pyplot as plt
from .AbstractFeature import AbstractFeature
from .DescriptiveStatisticsCalculators.OrdinalCalculator import OrdinalCalculator


class OrdinalFeature(AbstractFeature):

    _scale = 'Ordinal'

    def __init__(self, name, aggregated_data, ranks):
        self._ordered_data = []
        super(OrdinalFeature, self).__init__(name, aggregated_data)
        allowed_names = aggregated_data.keys()
        if len(ranks) != len(allowed_names):
            raise IndexError(f'Incorrect keys count in ranks expected: {len(allowed_names)} got: {len(ranks)}')
        for rank_name in ranks:
            if rank_name not in allowed_names:
                raise KeyError(f'No such value name {rank_name} found in all observation: {allowed_names}')
            self._ordered_data.append(copy.copy(rank_name))

    def get_stat_info(self):
        plt.figure(figsize=(35, 14))
        plt.rcParams.update({'font.size': 27})
        plt.bar(list(self._aggregated_data.keys()), self._aggregated_data.values(), color="#42aaf5")
        return {
            'Mode': OrdinalCalculator().calc_mode(self._aggregated_data),
            'Median': OrdinalCalculator().calc_median(self._ordered_data, self._aggregated_data),
            'Range':  OrdinalCalculator().calc_range(self._ordered_data)
                }
        # OrdinalCalculator().calc_max()
        # OrdinalCalculator().calc_min()

    @property
    def ordered_data(self):
        return self._ordered_data
