import pytest
from Core.ScaleFeaturesFactory import ScaleFeaturesFactory


class TestScaleFeaturesFactory:

    def setup(self):
        self.data_examples = [
            ['test nominal name', {'an_1': 1, 'an_2': 5}, 'ordinal', ['an_2', 'an_1']],
            ['test ordinal', {'an_1': 1, 'an_2': 5}, 'ordinal', ['an_2', 'an_1']],
            ['test name', {'an_0': 14}, 'ordinal', ['an_0']],
            ['Test nominal name with useless order', {'an_1': 1, 'an_2': 5}, 'nominal', ['an_2', 'an_1']],
            ['Test Interval scale', {'an_1': 34, 'avg2': 5, 'ang3': 7}, 'interval', {'an_1': 14.78, 'ang3': 0.98, 'avg2': 1.453}],
            ['Test Interval scale 2', {'an_11': 34, 'avg21': 5, 'ang31': 7, 'avg4': 50, 'ang5': 70}, 'interval',
             {'avg4': 12, 'ang5': 56, 'an_11': 76, 'ang31': 11, 'avg21': 9}]
        ]

    def test_scales_creation(self):
        none_formatter_feature_factory = ScaleFeaturesFactory('none')
        html_feature_factory = ScaleFeaturesFactory('html')

        for example in self.data_examples:
            scale = html_feature_factory.create_feature(example[0], example[1], example[2], example[3])
            assert scale.name == example[0]
            assert scale.aggregated_data == example[1]
            assert scale._scale.lower() == example[2]
            scale = none_formatter_feature_factory.create_feature(example[0], example[1], example[2], example[3])
            assert scale.name == example[0]
            assert scale.aggregated_data == example[1]
            assert scale._scale.lower() == example[2]

    def test_incorrect_formatter_exception(self):
        with pytest.raises(AttributeError,
                           match=r"Empty formatter is not allowed, please specify formatter. Allowed formatters \['html', 'none'\]"):
            html_feature_factory = ScaleFeaturesFactory('')
