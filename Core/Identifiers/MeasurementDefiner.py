from Core.Identifiers.CoreIdentifiers.OrdinaIdentifier import OrdinalIdentifier
from Core.Identifiers.CoreIdentifiers.NumericIdentifier import NumericIdentifier


class MeasurementDefiner:

    def __init__(self):
        self.numeric_identifier = NumericIdentifier()
        self.ordinal_identifier = OrdinalIdentifier()

    def define_measure(self, data_sign):
        if self.numeric_identifier.is_interval(data_sign):
            return 'interval'
        elif self.ordinal_identifier.is_ordinal(data_sign):
            return 'ordinal'
        else:
            return 'nominal'
