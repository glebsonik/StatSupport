from Identifiers import MeasuresManager as mm
import pandas as pd

# regexp = r'^[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+\s*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*$'
regexp = '(\d+(\.\d*)?)'

# print(list(map(
#     lambda m: tuple(filter(bool, m))[0], re.findall(regexp, '34 - 45.9')
# )))
# print(re.findall(regexp, '34. - 45.0'))
# print(re.findall(regexp, '12.5 - 30'))
# print(re.findall(regexp, '45 - 120'))
# print(re.findall(regexp, '34.9000 - 45.1'))
# print(re.findall(regexp, '34.5 - 45'))
# print(re.findall(regexp, '34 до 45'))
# print(re.findall(regexp, '34 to 45'))
# print(re.findall(regexp, '34 till 45'))
# print(re.findall(regexp, '34  45'))
# print(re.findall(regexp, '34 45'))
# print(re.findall(regexp, '34 – 45'))
# print(re.findall(regexp, '34 ііі 45'))
# print(re.findall(regexp, '34 дё 45'))
# print(re.findall(regexp, '1 34 дё 45'))
# print(re.findall(regexp, ' 22 34 дё 45'))
# print(re.findall(regexp, 'asdfasd 34 дё 45'))
# print(re.findall(regexp, '09 34 дё 45 9'))
# print(re.findall(regexp, 'asdfas 34 asdf 45'))
# print(re.findall(regexp, '34 hngvjhgfkjhgj- 45o'))
# print(re.findall(regexp, 'asdf 34 45 asdfasdfasd '))
# print(trueRegexp_1)
# print(trueRegexp_2)
# print(re.compile(trueRegexp_1.pattern + trueRegexp_2.pattern))

a = True
b = True
c = True

print(bool(a * b * c))
defer = mm.MeasuresManager("")

data = pd.read_csv("data/seps_utf.csv", ';')
data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
data = data.drop(['Оценка', 'Группа'], 1)
data = data.dropna()
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
ar = ["baba", "boey"]
print("".join(map(lambda x: x+"\n", ar)))