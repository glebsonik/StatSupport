from Core.MeasureSigns.NominalMeasureSign import NominalMeasureSign
from Core.MeasureSigns.Formatters.NominalHTMLFormatter import NominalHTMLFormatter


class SignFactory:
    def __init__(self, formatter):
        self.formatter = formatter if formatter else None

    def create_measure(self, sign_name, aggregated_values, measure_type):
        return getattr(self, f'create_{measure_type}_measure')(sign_name, aggregated_values)

    def create_nominal_measure(self, sign_name, aggregated_values):
        if (self.formatter == 'none') or not self.formatter:
            return NominalMeasureSign(sign_name, aggregated_values)
        elif self.formatter == 'html':
            return NominalHTMLFormatter(sign_name, aggregated_values)
        else:
            raise Exception(f'Unknown formatter {self.formatter}')
