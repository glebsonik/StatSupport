import pytest
import re
from Core.MeasureSigns.IntervalMeasureSign import IntervalMeasureSign
from Core.MeasureSigns.SelfStatisticCalculators.IntervalCalculator import IntervalCalculator
from unittest.mock import patch


class TestIntervalMeasureAndFormatter:

    def setup(self):
        self.correct_ordinal_data = [
            {
                "name": "Test interval data int",
                 "data": {
                     "First val": 5,
                     "Sec val": 67,
                     "Third val": 87
                 },
                 "ordered_data": {
                     "First val": 67,
                     "Sec val": 1,
                     "Third val": 9
                 },
                 'stat_res': {
                     'Mode': {"Third val": 87},
                     'Median': {"Third val": 9},
                     'Range': 67-1,
                     'Mean': 77/3,
                     'Variance': IntervalCalculator().calc_variance([67, 1, 9]),
                     'Standard Deviation': IntervalCalculator().calc_standard_deviation([67, 1, 9]),
                 }
            },
            {
                "name": "Test interval data float",
                 "data": {
                     "F_First": 1,
                     "F_Sec": 50,
                     "F_Third": 13
                 },
                 "ordered_data": {
                     "F_First": 5.09474,
                     "F_Sec": 0.9988,
                     "F_Third": 1.1123
                 },
                 'stat_res': {
                     'Mode': {"F_Sec": 50},
                     'Median': {"F_Third": 1.1123},
                     'Range': 5.09474 - 0.9988,
                     'Mean': (5.09474 + 0.9988 + 1.1123) / 3,
                     'Variance': IntervalCalculator().calc_variance([5.09474, 0.9988, 1.1123]),
                     'Standard Deviation': IntervalCalculator().calc_standard_deviation([5.09474, 0.9988, 1.1123]),
                 }
             },
            {
                "name": "Test interval data float even",
                "data": {
                    "Fe_First": 5,
                    "Fe_Sec": 95,
                    "Fe_Third": 12,
                    "Fe_Fourth": 12
                },
                "ordered_data": {
                    "Fe_First": 5.4,
                    "Fe_Sec": 95.01,
                    "Fe_Third": 12.2,
                    "Fe_Fourth": 12.09
                },
                'stat_res': {
                    'Mode': {"Fe_Sec": 95},
                    'Median': {'_': (95.01 + 12.2) / 2},
                    'Range': 95.01 - 5.4,
                    'Mean': round((5.4 + 95.01 + 12.2 + 12.09) / 4, 3),
                    'Variance': IntervalCalculator().calc_variance([5.4, 95.01, 12.2, 12.09]),
                    'Standard Deviation': IntervalCalculator().calc_standard_deviation([5.4, 95.01, 12.2, 12.09])
                }
            }
        ]

    def test_interval_measure(self):
        for data in self.correct_ordinal_data:
            sign = IntervalMeasureSign(data['name'],
                                       data['data'],
                                       data['ordered_data'])
            expected_ordered_data = {k: v for k, v in sorted(data['ordered_data'].items(), key=lambda item: item[1])}
            assert sign.name == data['name']

            print(f"ER: {data['data']} AR: {sign.aggregated_data}")
            assert sign.aggregated_data == data['data']

            print(f"ER: {expected_ordered_data} AR: {sign.ordered_data}")
            assert sign.ordered_data == expected_ordered_data

    @patch("matplotlib.pyplot.bar")
    def test_interval_stat_info(self, plot_stub):
        for data in self.correct_ordinal_data:
            sign = IntervalMeasureSign(data['name'],
                                       data['data'],
                                       data['ordered_data'])
            stat_res = sign.get_stat_info()
            for key in stat_res:
                print(f"{key} ER: {data['stat_res'][key]} AR: {stat_res[key]}")
                assert stat_res[key] == data['stat_res'][key]

