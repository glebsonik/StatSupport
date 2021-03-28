import pytest
from Core.SignFactory import SignFactory


class TestSignFactory:

    def setup(self):
        self.data_examples = [
            ['test nominal name', {'an_1': 1, 'an_2': 5}, 'ordinal', ['an_2', 'an_1']],
            ['test ordinal', {'an_1': 1, 'an_2': 5}, 'ordinal', ['an_2', 'an_1']],
            ['test name', {'an_0': 14}, 'ordinal', ['an_0']],
            ['Test nominal name with useless order', {'an_1': 1, 'an_2': 5}, 'nominal', ['an_2', 'an_1']]
        ]


    def test_ordinal_measure_creation(self):
        none_formatter_sign_factory = SignFactory('html')
        html_sign_factory = SignFactory('html')

        for example in self.data_examples:
            measure = html_sign_factory.create_measure(example[0], example[1], example[2], example[3])
            assert measure._name == example[0]
            assert measure._aggregated_data == example[1]
            assert measure._measure.lower() == example[2]
            measure = none_formatter_sign_factory.create_measure(example[0], example[1], example[2], example[3])
            assert measure._name == example[0]
            assert measure._aggregated_data == example[1]
            assert measure._measure.lower() == example[2]
