import pytest
from Core.SignFactory import SignFactory


class TestSignFactory:

    def setup(self):
        self.data_examples = [
            ['test nominal name', {'an_1': 1, 'an_2': 5}, 'ordinal', ['an_2', 'an_1']],
            ['test ordinal', {'an_1': 1, 'an_2': 5}, 'ordinal', ['an_2', 'an_1']],
            ['test name', {'an_0': 14}, 'ordinal', ['an_0']],
            ['Test nominal name with useless order', {'an_1': 1, 'an_2': 5}, 'nominal', ['an_2', 'an_1']],
            ['Test Interval measure', {'an_1': 34, 'avg2': 5, 'ang3': 7}, 'interval', {'an_1': 14.78, 'ang3': 0.98, 'avg2': 1.453}],
            ['Test Interval measure 2', {'an_11': 34, 'avg21': 5, 'ang31': 7, 'avg4': 50, 'ang5': 70}, 'interval',
             {'avg4': 12, 'ang5': 56, 'an_11': 76, 'ang31': 11, 'avg21': 9}]
        ]

    def test_measures_creation(self):
        none_formatter_sign_factory = SignFactory('none')
        html_sign_factory = SignFactory('html')

        for example in self.data_examples:
            measure = html_sign_factory.create_measure(example[0], example[1], example[2], example[3])
            assert measure.name == example[0]
            assert measure.aggregated_data == example[1]
            assert measure._measure.lower() == example[2]
            measure = none_formatter_sign_factory.create_measure(example[0], example[1], example[2], example[3])
            assert measure.name == example[0]
            assert measure.aggregated_data == example[1]
            assert measure._measure.lower() == example[2]

    def test_incorrect_formatter_exception(self):
        with pytest.raises(AttributeError,
                           match=r"Empty formatter is not allowed, please specify formatter. Allowed formatters \['html', 'none'\]"):
            html_sign_factory = SignFactory('')
