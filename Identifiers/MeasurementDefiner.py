from Identifiers.CoreIdentifiers import NumericIdentifier as nmi, OrdinaIdentifier as ori


class MeasurementDefiner:

    def __init__(self):
        self.numeric_identifier = nmi.NumericIdentifier()
        self.ordinal_identifier = ori.OrdinalIdentifier()

    def define_measure(self, data_sign):
        if self.is_interval(data_sign):
            return 'Interval'
        else:
            if self.ordinal_identifier.is_ordinal(data_sign):
                return 'Ordinal'
            else:
                return 'Nominal'

    def is_interval(self, data_sign):
        is_correct_interval = True
        for metric_value in list(data_sign.keys()):
            is_correct_interval *= self.numeric_identifier.is_number_or_num_interval(metric_value)
        return is_correct_interval
