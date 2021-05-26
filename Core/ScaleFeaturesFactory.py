from Core.FeaturesScales.NominalFeature import NominalFeature
from Core.FeaturesScales.OrdinalFeature import OrdinalFeature
from Core.FeaturesScales.IntervalFeature import IntervalFeature

from Core.FeaturesScales.Formatters.NominalHTMLFormatter import NominalHTMLFormatter
from Core.FeaturesScales.Formatters.OrdinalHTMLFormatter import OrdinalHTMLFormatter
from Core.FeaturesScales.Formatters.IntervalHTMLFormatter import IntervalHTMLFormatter


class ScaleFeaturesFactory:
    def __init__(self, formatter):
        allowed_formatters = list(list(self._allowed_data().items())[0][1].keys())
        if formatter == '':
            raise AttributeError(f'Empty formatter is not allowed, please specify formatter. Allowed formatters {allowed_formatters}')
        if formatter.lower() in allowed_formatters:
            self.formatter = formatter.lower()
        else:
            raise AttributeError(f'No such formatter "{formatter}". Allowed formatters #{allowed_formatters}')

    def create_feature(self, feature_name, observation, scale_type, values=None):
        if scale_type == 'nominal':
            return self.create_nominal_feature(feature_name, observation)
        elif scale_type == 'ordinal':
            return self.create_ordinal_feature(feature_name, observation, values)
        elif scale_type == 'interval':
            return self.create_interval_feature(feature_name, observation, values)
        else:
            raise NameError(f'No such scale {scale_type}')

    def create_nominal_feature(self, features_name, raw_observation):
        feature_class = self._allowed_data()['nominal'][self.formatter]
        if not feature_class:
            raise AttributeError(
                f"Wrong nominal formatter: {self.formatter}, allowed formatters {self._allowed_data()['nominal'].keys}")
        return feature_class(features_name, raw_observation)

    def create_ordinal_feature(self, features_name, raw_observation, ranks):
        feature_class = self._allowed_data()['ordinal'][self.formatter]
        if not feature_class:
            raise AttributeError(
                f"Wrong ordinal formatter: {self.formatter}, allowed formatters {self._allowed_data()['ordinal'].keys}")
        return feature_class(features_name, raw_observation, ranks)

    def create_interval_feature(self, features_name, raw_observation, ranks):
        feature_class = self._allowed_data()['interval'][self.formatter]
        if not feature_class:
            raise AttributeError(
                f"Wrong interval formatter: {self.formatter}, allowed formatters {self._allowed_data()['ordinal'].keys}")
        print("Creating: ", features_name, " =====***======\n", raw_observation, "****====_____\n", ranks)
        return feature_class(features_name, raw_observation, ranks)

    def _allowed_data(self):
        return {
            'nominal': {'html': NominalHTMLFormatter, 'none': NominalFeature},
            'ordinal': {'html': OrdinalHTMLFormatter, 'none': OrdinalFeature},
            'interval': {'html': IntervalHTMLFormatter, 'none': IntervalFeature}
        }
