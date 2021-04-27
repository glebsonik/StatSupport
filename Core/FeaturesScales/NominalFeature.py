from .DescriptiveStatisticsCalculators.NominalCalculator import NominalCalculator
from .AbstractFeature import AbstractFeature
import matplotlib.pyplot as plt


class NominalFeature(AbstractFeature):

    _scale = 'Nominal'

    def get_stat_info(self):
        plt.figure(figsize=(35, 14))
        plt.rcParams.update({'font.size': 27})
        plt.bar(list(self._aggregated_data.keys()), self._aggregated_data.values(), color="orange")
        return {"Mode:": NominalCalculator().calc_mode(self._aggregated_data)}
