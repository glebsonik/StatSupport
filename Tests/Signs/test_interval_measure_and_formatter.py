import pytest
import re
from Core.FeaturesScales.IntervalFeature import IntervalFeature
from Core.FeaturesScales.DescriptiveStatisticsCalculators.IntervalCalculator import IntervalCalculator
from unittest.mock import patch


class TestIntervalscaleAndFormatter:

    def setup(self):
        self.correct_ordinal_data = [
            {
                "name": "Test interval data int",
                "aggregated_data": {
                    "First val": 5,
                    "Sec val": 67,
                    "Third val": 87
                },
                "ordered_data": {
                    "First val": 67,
                    "Sec val": 1,
                    "Third val": 9
                },
                "expected_ordered_data": [
                    ("Sec val", 1),
                    ("Third val", 9),
                    ("First val", 67)
                ],
                'stat_res': {
                    'Mode': {"Third val": 87},
                    'Median': {"Third val": 9},
                    'Range': 67 - 1,
                    'Mean': 77 / 3,
                    'Variance': IntervalCalculator().calc_variance([67, 1, 9]),
                    'Standard Deviation': IntervalCalculator().calc_standard_deviation([67, 1, 9]),
                }
            },
            {
                "name": "Test interval data float",
                "aggregated_data": {
                    "F_First": 1,
                    "F_Sec": 50,
                    "F_Third": 13
                },
                "ordered_data": {
                    "F_First": 5.09474,
                    "F_Sec": 0.9988,
                    "F_Third": 1.1123
                },
                "expected_ordered_data": [
                    ("F_Sec", 0.9988),
                    ("F_Third", 1.1123),
                    ("F_First", 5.09474)
                ],
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
                "aggregated_data": {
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
                "expected_ordered_data": [
                    ("Fe_First", 5.4),
                    ("Fe_Fourth", 12.09),
                    ("Fe_Third", 12.2),
                    ("Fe_Sec", 95.01)
                ],
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

    def pr_list(self, hss):
        res = []
        for val in hss:
            for y in range(hss[val]):
                res.append(val)
        return res

    def test_interval_scale(self):
        for data in self.correct_ordinal_data:
            raw_data = self.pr_list(data['aggregated_data'])
            feature = IntervalFeature(data['name'],
                                      raw_data,
                                      data['ordered_data'])
            # expected_ordered_data = {k: v for k, v in sorted(data['ordered_data'].items(), key=lambda item: item[1])}
            expected_ordered_data = data['expected_ordered_data']
            print(expected_ordered_data)
            assert feature.name == data['name']

            print(f"ER: {data['aggregated_data']} AR: {feature.aggregated_data}")
            assert feature.aggregated_data == data['aggregated_data']
            assert feature.data == raw_data

            print(f"ER: {expected_ordered_data} AR: {feature.ordered_data}")
            actual_ord_data = list(feature.ordered_data.items())
            for i in range(0, len(actual_ord_data)):
                print(f'Case {i}. AR: {actual_ord_data[i]} ER: {expected_ordered_data[i]}')
                assert actual_ord_data[i] == expected_ordered_data[i]

    @patch("matplotlib.pyplot.bar")
    def test_interval_stat_info(self, plot_stub):
        for data in self.correct_ordinal_data:
            raw_data = self.pr_list(data['aggregated_data'])
            feature = IntervalFeature(data['name'],
                                      raw_data,
                                      data['ordered_data'])
            stat_res = feature.get_stat_info()
            for key in stat_res:
                print(f"{key} ER: {data['stat_res'][key]} AR: {stat_res[key]}")
                assert stat_res[key] == data['stat_res'][key]
