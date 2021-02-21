import re


class NumericIdentifier:

    # intervalRegexp = re.compile(r'^[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+\s*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*$')
    float_text_regexp = re.compile(r'^.{0,12}\d+[.,]\d*.{0,9}$')

    def is_number_or_num_interval(self, value):
        if type(value) == float:
            return True
        else:
            if re.match(self.float_text_regexp, value):
                return True
            else:
                return False

    # def validate_interval(self, value):
    #     number_regexp = re.compile(r'(\d+(\.\d*)?)')
    #     string_numbers = list(map(lambda m: tuple(filter(bool, m))[0], re.findall(number_regexp, value)))
    #     if float(string_numbers[0]) < float(string_numbers[1]):
    #         return True
    #     else:
    #         return False
