from Core.MeasureSigns.SelfStatisticCalculators.NominalCalculator import NominalCalculator
import matplotlib.pyplot as plt

class NominalMeasureSign:

    _name = None
    _aggregated_data = {}

    def __init__(self, sign_name, aggregated_data):
        self._name = sign_name
        self._aggregated_data = aggregated_data

    def get_stat_info(self):
        plt.figure(figsize=(35, 14))
        plt.rcParams.update({'font.size': 27})
        plt.bar(list(self._aggregated_data.keys()), self._aggregated_data.values(), color="orange")
        return {"Mode:": NominalCalculator.calc_mode(self._aggregated_data)}

    @property
    def name(self):
        return self._name

    @property
    def aggregated_data(self):
        return self._aggregated_data
