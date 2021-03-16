from .AbstractSign import AbstractMeasureSign
from .SelfStatisticCalculators.OrdinalCalculator import OrdinalCalculator


class OrdinalMeasureSign(AbstractMeasureSign):

    def __init__(self, name, aggregated_data, ranks):
        super(OrdinalMeasureSign, self).__init__(name, aggregated_data)
        for sign in ranks:
            raise KeyError("No such sign in ")
            ranks[sign_name]


    def get_stat_info(self):
        OrdinalCalculator().calc_mode(self._aggregated_data)
        OrdinalCalculator().calc_median()
        OrdinalCalculator().calc_max()
        OrdinalCalculator().calc_min()
