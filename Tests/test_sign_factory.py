import pytest
from Core.SignFactory import SignFactory

class test_sign_factory:

    def test_ordinal_measure_creation(self):
        sign_factory = SignFactory('html')
        print(sign_factory.create_measure('test name',
                                          {'an_1': 1,
                                           'an_2': 5},
                                          'ordinal'))
