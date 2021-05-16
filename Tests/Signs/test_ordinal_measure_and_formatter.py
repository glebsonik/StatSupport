import pytest
import re
from Core.FeaturesScales.OrdinalFeature import OrdinalFeature
from Core.FeaturesScales.Formatters.OrdinalHTMLFormatter import OrdinalHTMLFormatter
from unittest.mock import patch


class TestOrdinalscaleAndFormatter:

    def setup(self):
        self.correct_ordinal_data = [{"name": "Test ordinal Data",
                                      "aggregated_data": {
                                          "Yes": 5,
                                          "No": 67,
                                          "Maybe": 87
                                      },
                                      "ranks": ["No", "Maybe", "Yes"],
                                      'range': 2,
                                      'mode': {"Maybe": 87},
                                      'median': {"Maybe": 87}
                                      }, {"name": "Тест Ранговой шкалі",
                                          "aggregated_data": {
                                              89: 5,
                                              "No": 67,
                                              "Maybe": 87
                                          },
                                          "ranks": ["No", "Maybe", 89]
                                          },
                                     {"name": "Test ordinal Data",
                                      "aggregated_data": {
                                          "Maybe": 87,
                                          "Yes": 5,
                                          'Iess': 1
                                      },
                                      "ranks": ["Maybe", "Yes", 'Iess']
                                      },
                                     {"name": "Test ordinal Data",
                                      "aggregated_data": {
                                          "Yes": 5,
                                          "No": 67,
                                          "Maybe": 87
                                      },
                                      "ranks": ["Yes", "No", "Maybe"]
                                      }, {"name": "Test ordinal Data",
                                          "aggregated_data": {
                                              "Yes": 5,
                                              "No": 67,
                                              "Maybe": 87
                                          },
                                          "ranks": ["No", "Maybe", "Yes"]
                                          }
                                     ]

    def pr_list(self, hss):
        res = []
        for val in hss:
            for y in range(hss[val]):
                res.append(val)
        return res

    def test_ordinal_init(self):
        for data_example in self.correct_ordinal_data:
            print('ex: ', data_example)
            raw_data = self.pr_list(data_example['aggregated_data'])
            feature = OrdinalFeature(data_example['name'],
                                     raw_data,
                                     data_example['ranks'])
            print(feature.name)
            print(feature.aggregated_data)
            print(feature._ordered_data)
            assert feature.name == data_example['name']
            assert feature._aggregated_data == data_example['aggregated_data']
            assert feature._ordered_data == data_example['ranks']

    def test_ordinal_data_calculation(self):
        # for data_example in self.correct_ordinal_data:
        data_example = self.correct_ordinal_data[0]
        raw_data = self.pr_list(data_example['aggregated_data'])
        stat_data = OrdinalFeature(data_example['name'],
                                   raw_data,
                                   data_example['ranks']).get_stat_info()
        print('er: ', data_example)
        print('ar: ', stat_data)
        assert stat_data['Mode'] == data_example['mode']
        assert stat_data['Median'] == data_example['median']
        assert stat_data['Range'] == data_example['range']

    @patch("matplotlib.pyplot.bar")
    def test_html_ordinal_init(self, plot_stub):
        for data_example in self.correct_ordinal_data:
            print('ex: ', data_example)
            raw_data = self.pr_list(data_example['aggregated_data'])
            feature = OrdinalHTMLFormatter(data_example['name'],
                                           raw_data,
                                           data_example['ranks'])
            print(feature.name)
            print(feature.aggregated_data)
            print(feature._ordered_data)
            assert feature.name == data_example['name']
            assert feature._aggregated_data == data_example['aggregated_data']
            assert feature._ordered_data == data_example['ranks']
            print(feature.name)
            print(feature.f_aggregated_data)
            assert re.match(f"<.*>{data_example['name']}</.*>", feature.f_name)
            print(feature.f_get_stat_info())
            # assert re.match(f"<.*>{data_example['data']}</.*>", feature.name)
            # assert feature._aggregated_data == data_example['data']
            # assert feature._ordered_data == data_example['ranks']

    def test_html_ordinal_data_calculation(self):
        # for data_example in self.correct_ordinal_data:
        data_example = self.correct_ordinal_data[0]
        raw_data = self.pr_list(data_example['aggregated_data'])
        stat_data = OrdinalFeature(data_example['name'],
                                   raw_data,
                                   data_example['ranks']).get_stat_info()
        print('er: ', data_example)
        print('ar: ', stat_data)
        assert stat_data['Mode'] == data_example['mode']
        assert stat_data['Median'] == data_example['median']
        assert stat_data['Range'] == data_example['range']
