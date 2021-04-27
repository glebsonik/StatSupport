import pytest
import pandas as pd
from Core.FeaturesModel import FeaturesModel
from Core.FeaturesScales.NominalFeature import NominalFeature


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


    def test_scale_get_item(self):
        scale_manager = FeaturesModel(self.test_data, 'html')
        assert scale_manager[self.test_cols_names[0]].name == self.test_cols_names[0]
        assert scale_manager[self.test_cols_names[1]].name == self.test_cols_names[1]
        assert scale_manager[self.test_cols_names[2]].name == self.test_cols_names[2]


    def test_scales_set_item(self):
        test_feature_name = 'Some coool new name'
        test_feature = NominalFeature('Some coool new name', {'Answ_1': 5, 'Answ_2': 6, 'Answ_3': 9})
        scale_manager = FeaturesModel(self.test_data, 'html')
        print('features names before: ', list(map(lambda x: x.name, scale_manager.features)))
        initial_length = len(scale_manager.features)
        scale_manager[self.test_cols_names[2]] = test_feature
        print('features names after: ', list(map(lambda x: x.name, scale_manager.features)))
        assert 'Some coool new name', scale_manager[test_feature_name]._name
        assert len(scale_manager.features), initial_length
        print(scale_manager.raw_features_names())

    def test_set_error(self):
        scale_manager = FeaturesModel(self.test_data, 'html')
        with pytest.raises(NameError, match=r"No such feature found by: .*"):
            scale_manager['Wrong item name']
