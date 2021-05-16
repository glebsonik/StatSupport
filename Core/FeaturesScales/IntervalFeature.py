from .AbstractFeature import AbstractFeature
from .DescriptiveStatisticsCalculators.IntervalCalculator import IntervalCalculator
import matplotlib.pyplot as plt
import copy


class IntervalFeature(AbstractFeature):

    _scale = 'Interval'

    def __init__(self, name, data, ranks: dict):
        if not(ranks.__class__ == dict):
            raise AttributeError(f"Non dict ranks is not allowed {ranks.__class__}")
        self._ordered_data = {}
        super(IntervalFeature, self).__init__(name, data)
        allowed_names = self.aggregated_data.keys()
        if len(ranks) != len(allowed_names):
            raise IndexError(f'Incorrect keys count in ranks expected: {len(allowed_names)} got: {len(ranks)}')
        for rank_name in ranks:
            if rank_name not in allowed_names:
                raise KeyError(f'No such value name: {rank_name} found in all observation: {allowed_names}')
            self._ordered_data[rank_name] = copy.copy(ranks[rank_name])
        self._ordered_data = {k: v for k, v in sorted(self._ordered_data.items(), key=lambda item: item[1])}

    def get_stat_info(self):
        plt.figure(figsize=(35, 14))
        plt.rcParams.update({'font.size': 27})
        plt.bar(list(self._aggregated_data.keys()), self._aggregated_data.values(), color="#c90065")
        calculator = IntervalCalculator()
        list_of_values = list(self._ordered_data.values())
        return {
            'Mode': calculator.calc_mode(self._aggregated_data),
            'Median': calculator.calc_median(self._ordered_data, self._aggregated_data),
            'Range': calculator.calc_range(sorted(list_of_values)),
            'Mean': calculator.calc_mean(list_of_values),
            'Variance': calculator.calc_variance(list_of_values),
            'Standard Deviation': calculator.calc_standard_deviation(list_of_values)
        }

    @property
    def ordered_data(self):
        return self._ordered_data
    # def __ident_order(self):
    #     for feature_name in self.f_aggregated_data:


