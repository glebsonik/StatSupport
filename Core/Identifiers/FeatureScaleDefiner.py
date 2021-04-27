from Core.Identifiers.CoreIdentifiers.OrdinaIdentifier import OrdinalIdentifier
from Core.Identifiers.CoreIdentifiers.IntervalIdentifier import IntervalIdentifier


class FeatureScaleDefiner:

    def __init__(self):
        self.numeric_identifier = IntervalIdentifier()
        self.ordinal_identifier = OrdinalIdentifier()

    def define_scale(self, raw_data_observation):
        if self.numeric_identifier.is_interval(raw_data_observation):
            return 'interval'
        elif self.ordinal_identifier.is_ordinal(raw_data_observation):
            return 'ordinal'
        else:
            return 'nominal'
