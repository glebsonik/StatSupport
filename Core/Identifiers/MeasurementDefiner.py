from Core.Identifiers.CoreIdentifiers.OrdinaIdentifier import OrdinalIdentifier
from Core.Identifiers.CoreIdentifiers.IntervalIdentifier import IntervalIdentifier


class MeasurementDefiner:

    def __init__(self):
        self.numeric_identifier = IntervalIdentifier()
        self.ordinal_identifier = OrdinalIdentifier()

    def define_measure(self, data_sign):
        if self.numeric_identifier.is_interval(data_sign):
            return 'interval'
        elif self.ordinal_identifier.is_ordinal(data_sign):
            return 'ordinal'
        else:
            return 'nominal'
