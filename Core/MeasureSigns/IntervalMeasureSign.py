from .AbstractSign import AbstractMeasureSign


class IntervalMeasureSign(AbstractMeasureSign):

    sign_name = None
    aggregated_data = None
    _measure = 'Interval'

    def get_stat_info(self):
        raise NotImplementedError("Abstract class has no methods implementation")
    # def __ident_order(self):
    #     for sign_name in self.aggregated_data:


