import re
from Core.Service.DataAggregator import DataAggregator

class IntervalIdentifier:

    # intervalRegexp = re.compile(r'^[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+\s*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*$')
    float_text_regexp = re.compile(r'^.{0,12}\d+[.,]\d*.{0,9}$')

    def is_interval(self, raw_data_feature: list):
        data_feature = DataAggregator.aggregate_list(raw_data_feature)
        is_correct_interval = True
        for metric_value in list(data_feature.keys()):
            is_correct_interval *= self.__is_number_or_num_interval(metric_value)
        return is_correct_interval

    def __is_number_or_num_interval(self, value):
        if type(value) == float:
            return True
        else:
            if re.match(self.float_text_regexp, str(value)):
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
