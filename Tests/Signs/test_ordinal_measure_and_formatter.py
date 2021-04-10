import pytest
import re
from Core.MeasureSigns.OrdinalMeasureSign import OrdinalMeasureSign
from Core.MeasureSigns.Formatters.OrdinalHTMLFormatter import OrdinalHTMLFormatter
from unittest.mock import patch


class TestOrdinalMeasureAndFormatter:

    def setup(self):
        self.correct_ordinal_data = [{"name": "Test ordinal Data",
                                      "data": {
                                          "Yes": 5,
                                          "No": 67,
                                          "Maybe": 87
                                      },
                                      "ranks": ["No", "Maybe", "Yes"],
                                      'range': 2,
                                      'mode': {"Maybe": 87},
                                      'median': {"Maybe": 87}
                                      }, {"name": "Тест Ранговой шкалі",
                                          "data": {
                                              89: 5,
                                              "No": 67,
                                              "Maybe": 87
                                          },
                                          "ranks": ["No", "Maybe", 89]
                                          },
                                     {"name": "Test ordinal Data",
                                      "data": {
                                          "Maybe": 87,
                                          "Yes": 5,
                                          'Iess': 1
                                      },
                                      "ranks": ["Maybe", "Yes", 'Iess']
                                      },
                                     {"name": "Test ordinal Data",
                                      "data": {
                                          "Yes": 5,
                                          "No": 67,
                                          "Maybe": 87
                                      },
                                      "ranks": ["Yes", "No", "Maybe"]
                                      }, {"name": "Test ordinal Data",
                                          "data": {
                                              "Yes": 5,
                                              "No": 67,
                                              "Maybe": 87
                                          },
                                          "ranks": ["No", "Maybe", "Yes"]
                                          }
                                     ]

    def test_ordinal_init(self):
        for data_example in self.correct_ordinal_data:
            print('ex: ', data_example)

            sign = OrdinalMeasureSign(data_example['name'],
                                      data_example['data'],
                                      data_example['ranks'])
            print(sign.name)
            print(sign.aggregated_data)
            print(sign._ordered_data)
            assert sign.name == data_example['name']
            assert sign._aggregated_data == data_example['data']
            assert sign._ordered_data == data_example['ranks']

    def test_ordinal_data_calculation(self):
        # for data_example in self.correct_ordinal_data:
        data_example = self.correct_ordinal_data[0]
        stat_data = OrdinalMeasureSign(data_example['name'],
                                       data_example['data'],
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

            sign = OrdinalHTMLFormatter(data_example['name'],
                                        data_example['data'],
                                        data_example['ranks'])
            print(sign.name)
            print(sign.aggregated_data)
            print(sign._ordered_data)
            assert sign.name == data_example['name']
            assert sign._aggregated_data == data_example['data']
            assert sign._ordered_data == data_example['ranks']
            print(sign.name)
            print(sign.f_aggregated_data)
            assert re.match(f"<.*>{data_example['name']}</.*>", sign.f_name)
            print(sign.f_get_stat_info())
            # assert re.match(f"<.*>{data_example['data']}</.*>", sign.name)
            # assert sign._aggregated_data == data_example['data']
            # assert sign._ordered_data == data_example['ranks']


    def test_html_ordinal_data_calculation(self):
        # for data_example in self.correct_ordinal_data:
        data_example = self.correct_ordinal_data[0]
        stat_data = OrdinalMeasureSign(data_example['name'],
                                       data_example['data'],
                                       data_example['ranks']).get_stat_info()
        print('er: ', data_example)
        print('ar: ', stat_data)
        assert stat_data['Mode'] == data_example['mode']
        assert stat_data['Median'] == data_example['median']
        assert stat_data['Range'] == data_example['range']
