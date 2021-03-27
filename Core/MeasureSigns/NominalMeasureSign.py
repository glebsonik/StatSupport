from .SelfStatisticCalculators.NominalCalculator import NominalCalculator
from .AbstractSign import AbstractMeasureSign
import matplotlib.pyplot as plt


class NominalMeasureSign(AbstractMeasureSign):

    _measure = 'Nominal'

    def get_stat_info(self):
        plt.figure(figsize=(35, 14))
        plt.rcParams.update({'font.size': 27})
        plt.bar(list(self._aggregated_data.keys()), self._aggregated_data.values(), color="orange")
        return {"Mode:": NominalCalculator().calc_mode(self._aggregated_data)}
