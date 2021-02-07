from Identifiers import MeasurementDefiner as md

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
defer = md.MeasurementDefiner()

hs = {'Содержание дисциплины соответствовало заявленному в программе дисциплины': {'Полностью согласен': 38,
  'Согласен': 12,
  'Не определился': 1}}

print(defer.numeric_identifier.validate_interval("0-30"))
hs['popa'] = 1
print(hs)
# pd.DataFrame.from_dict