from Core.MeasureSigns.NominalMeasureSign import NominalMeasureSign
from Core.MeasureSigns.OrdinalMeasureSign import OrdinalMeasureSign

from Core.MeasureSigns.Formatters.NominalHTMLFormatter import NominalHTMLFormatter
from Core.MeasureSigns.Formatters.OrdinalHTMLFormatter import OrdinalHTMLFormatter


class SignFactory:
    def __init__(self, formatter):
        if formatter == '':
            raise AttributeError('Empty formatter is not allowed, please specify formatter or pass None arg')

        self.formatter = formatter if formatter.lower() else 'none'

    def create_measure(self, sign_name, aggregated_values, raw_measure_type, values=None):
        measure_type = raw_measure_type.lower()
        if measure_type == 'nominal':
            return self.create_nominal_measure(sign_name, aggregated_values)
        elif measure_type == 'ordinal':
            return self.create_ordinal_measure(sign_name, aggregated_values, values)
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
                f"Wrong nominal formatter: {self.formatter}, allowed formatters {self._allowed_data()['ordinal'].keys}")
        return measure_class(sign_name, aggregated_values, ranks)

    def _allowed_data(self):
        return {
            'nominal': {'html': NominalHTMLFormatter, 'none': NominalMeasureSign},
            'ordinal': {'html': OrdinalHTMLFormatter, 'none': OrdinalMeasureSign}
        }