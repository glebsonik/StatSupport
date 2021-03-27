# from Core.Identifiers import MeasuresManager as mm
from Core.MeasureSigns.Formatters.NominalHTMLFormatter import NominalHTMLFormatter
from Core.SignFactory import SignFactory
from Core.MeasuresManager import MeasuresManager
import pandas as pd
import numpy as np
# import Core.TestImposter
# regexp = r'^[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+\s*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*$'

# print(bool(a * b * c))
# defer = mm.MeasuresManager("")
# imp.TestImposter()
# data = pd.read_csv("data/seps_utf.csv", ';')
# data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
# data = data.drop(['Оценка', 'Группа'], 1)
# data = data.dropna()
  # {'Содержание дисциплины соответствовало заявленному в программе дисциплины': {'Полностью согласен': 38,
  # 'Согласен': 12,
  # 'Не определился': 1}}
# print(data.columns)
# print(str(data['Место дисциплины в программе обучения обосновано'].mode()))
# for h in hs:
#   print(h)

# print(defer.define_measures(hs))

# hs['popa'] = 1
# print(list(hs.keys()))
# # pd.DataFrame.from_dict
# test_var = "init val"
#
# test_hs = {"val":{"inv":7}, "or": 8}
# def scoping_test(nm):
#   nm["val"] = 6
#
# scoping_test(test_hs)
# print(test_hs)
# ar = ["baba", "boey"]
# print("".join(map(lambda x: x+"\n", ar)))

# class TestClassA:
#
#     def __init__(self, x):
#         self.__x = x
#
#     def raw_x(self):
#         return self.__x
#
#     @property
#     def x(self):
#         return self.__x + 9
#
#     @x.setter
#     def x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
sign = SignFactory('html').create_measure("Some cool name",
                                          {"Посильная": 34, "Ze Loop Ah": 12, "TestVarSign": 45},
                                          'nominal')
sign_2 = SignFactory('html').create_measure("2 name",
                                          {"asdf ": 34, "Ze Ah": 12, "VSign": 45},
                                          'nominal')
# print(sign.aggregated_data)
# print(sign.name)
# print(sign._name)
# print(sign._aggregated_data)
# print(sign.get_stat_info())
data = pd.read_csv("data/seps_utf.csv", ';')
data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
data = data.drop(['Оценка', 'Группа'], 1)
data = data.dropna()

# mm = MeasuresManager(data)
# print(mm['Перед изучением дисциплины [был ли у Вас соответствующий практический опыт]'].get_stat_info())
# print(mm.raw_signs_names())
ar = ['pipa','popa']
ar_2 = list(map(lambda x: x + 'pip', ar))

print(ar)
print(ar_2)


class TestCls:

    def invoke(self, nam):
        nam.name += 'pipa'

    def test_m(self):
        print('test_m')


class ModelCls:
    name = 'test'

cls = TestCls()
model = ModelCls()
# cls.invoke('test_m')

cls.invoke(model)
print(model.name)
