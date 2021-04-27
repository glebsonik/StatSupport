from Core.MeasureSigns.NominalMeasureSign import NominalMeasureSign
from Core.MeasureSigns.OrdinalMeasureSign import OrdinalMeasureSign
from Core.MeasureSigns.IntervalMeasureSign import IntervalMeasureSign

from Core.MeasureSigns.Formatters.NominalHTMLFormatter import NominalHTMLFormatter
from Core.MeasureSigns.Formatters.OrdinalHTMLFormatter import OrdinalHTMLFormatter
from Core.MeasureSigns.Formatters.IntervalHTMLFormatter import IntervalHTMLFormatter


class SignFactory:
    def __init__(self, formatter):
        allowed_formatters = list(list(self._allowed_data().items())[0][1].keys())
        if formatter == '':
            raise AttributeError(f'Empty formatter is not allowed, please specify formatter. Allowed formatters {allowed_formatters}')
        if formatter.lower() in allowed_formatters:
            self.formatter = formatter.lower()
        else:
            raise AttributeError(f'No such formatter "{formatter}". Allowed formatters #{allowed_formatters}')

    def create_measure(self, sign_name, aggregated_values, measure_type, values=None):
        if measure_type == 'nominal':
            return self.create_nominal_measure(sign_name, aggregated_values)
        elif measure_type == 'ordinal':
            return self.create_ordinal_measure(sign_name, aggregated_values, values)
        elif measure_type == 'interval':
            return self.create_interval_measure(sign_name, aggregated_values, values)
        else:
            raise NameError(f'No such measure {measure_type}')

    def create_nominal_measure(self, sign_name, aggregated_values):
        measure_class = self._allowed_data()['nominal'][self.formatter]
        if not measure_class:
            raise AttributeError(
                f"Wrong nominal formatter: {self.formatter}, allowed formatters {self._allowed_data()['nominal'].keys}")
        return measure_class(sign_name, aggregated_values)

    def create_ordinal_measure(self, sign_name, aggregated_values, ranks):
        measure_class = self._allowed_data()['ordinal'][self.formatter]
        if not measure_class:
            raise AttributeError(
                f"Wrong ordinal formatter: {self.formatter}, allowed formatters {self._allowed_data()['ordinal'].keys}")
        return measure_class(sign_name, aggregated_values, ranks)

    def create_interval_measure(self, sign_name, aggregated_values, ranks):
        measure_class = self._allowed_data()['interval'][self.formatter]
        if not measure_class:
            raise AttributeError(
                f"Wrong interval formatter: {self.formatter}, allowed formatters {self._allowed_data()['ordinal'].keys}")
        return measure_class(sign_name, aggregated_values, ranks)

    def _allowed_data(self):
        return {
            'nominal': {'html': NominalHTMLFormatter, 'none': NominalMeasureSign},
            'ordinal': {'html': OrdinalHTMLFormatter, 'none': OrdinalMeasureSign},
            'interval': {'html': IntervalHTMLFormatter, 'none': IntervalMeasureSign}
        }
