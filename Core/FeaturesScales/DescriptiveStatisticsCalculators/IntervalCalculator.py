from functools import reduce
from Core.FeaturesScales.DescriptiveStatisticsCalculators.OrdinalCalculator import OrdinalCalculator


class IntervalCalculator(OrdinalCalculator):

    def calc_median(self, order_features_data: dict, aggregated_data: dict):
        data_values = list(order_features_data.values())
        if len(data_values) % 2 != 0:
            median_value = data_values[int((len(order_features_data) + 1) / 2) - 1]
        else:
            middle_val_1 = data_values[int(len(order_features_data) / 2)]
            middle_val_2 = data_values[int(len(order_features_data) / 2) + 1]
            median_value = (middle_val_1 + middle_val_2) / 2
        key_for_val = [key for (key, value) in order_features_data.items() if value == median_value]
        return {key_for_val[0]: median_value} if len(key_for_val) > 0 else {'_': median_value}

    def calc_range(self, features_data: list):
        return (features_data[len(features_data) - 1] - features_data[0]) if len(features_data) > 1 else 0

    def calc_mean(self, values: list):
        return reduce(lambda x, y: x + y, values)/len(values)

    def calc_variance(self, values: list):
        mean = self.calc_mean(values)
        return round(reduce(lambda x, y: x + y, list(map(lambda x: (x - mean) ** 2, values))) / (len(values) - 1), 10)

    def calc_standard_deviation(self, values: list):
        return pow(self.calc_variance(values), 0.5)
