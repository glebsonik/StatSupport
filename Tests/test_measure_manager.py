import pytest
import pandas as pd
from Core.MeasuresManager import MeasuresManager
from Core.MeasureSigns.NominalMeasureSign import NominalMeasureSign


class TestUM:

    def teardown(self):
        print("basic teardown into class")

    def setup_class(cls):
        print("class setup")

    def teardown_class(cls):
        print("class teardown")

    def setup_method(self, method):
        print("method setup")

    def teardown_method(self, method):
        print("method teardown")

    def setup(self):
        data = pd.read_csv("./data/seps_utf.csv", ';')
        data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
        data = data.drop(['Оценка', 'Группа'], 1)
        data = data.dropna()
        self.test_data = data
        self.test_cols_names = ['Содержание дисциплины соответствовало заявленному в программе дисциплины',
                                'Место дисциплины в программе обучения обосновано',
                                'Доступ к материалам дисциплины предоставлялся вовремя']


    def test_measure_get_item(self):
        measure_manager = MeasuresManager(self.test_data, 'html')
        assert measure_manager[self.test_cols_names[0]].name == self.test_cols_names[0]
        assert measure_manager[self.test_cols_names[1]].name == self.test_cols_names[1]
        assert measure_manager[self.test_cols_names[2]].name == self.test_cols_names[2]


    def test_measures_set_item(self):
        test_sign_name = 'Some coool new name'
        test_sign = NominalMeasureSign('Some coool new name', {'Answ_1': 5, 'Answ_2': 6, 'Answ_3': 9})
        measure_manager = MeasuresManager(self.test_data, 'html')
        print('Signs names before: ', list(map(lambda x: x.name, measure_manager.signs)))
        initial_length = len(measure_manager.signs)
        measure_manager[self.test_cols_names[2]] = test_sign
        print('Signs names after: ', list(map(lambda x: x.name, measure_manager.signs)))
        assert 'Some coool new name', measure_manager[test_sign_name]._name
        assert len(measure_manager.signs), initial_length
        print(measure_manager.raw_signs_names())

    def test_set_error(self):
        measure_manager = MeasuresManager(self.test_data, 'html')
        with pytest.raises(NameError, match=r"No such sign found by: .*"):
            measure_manager['Wrong item name']
