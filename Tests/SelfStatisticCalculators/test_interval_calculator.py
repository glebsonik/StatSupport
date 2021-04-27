import pytest
import re
from Core.FeaturesScales.IntervalFeature import IntervalFeature
from Core.FeaturesScales.DescriptiveStatisticsCalculators.IntervalCalculator import IntervalCalculator
from unittest.mock import patch


class TestIntervalscaleAndFormatter:

    def setup(self):
        self.correct_data = [{'data': [1, 2, 3], 'variance': 1, 'deviation': 1},
                             {'data': [56, 78, 99], 'variance': 462.333, 'deviation': 21.502},
                             {'data': [2.7, 123.99, 12.90005], 'variance': 4526.047, 'deviation': 67.276}]

    def test_range(self):
        for data in self.correct_data:
            assert IntervalCalculator().calc_range(data['data']) == (data['data'][2] - data['data'][0])

    def test_variance_calculation(self):
        for data in self.correct_data:
            assert round(IntervalCalculator().calc_variance(data['data']), 3) == data['variance']

    def test_standard_deviation_calculation(self):
        for data in self.correct_data:
            assert round(IntervalCalculator().calc_standard_deviation(data['data']), 3) == data['deviation']
