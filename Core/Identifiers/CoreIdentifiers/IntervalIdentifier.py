import re
from Core.Service.DataAggregator import DataAggregator

class IntervalIdentifier:

    # intervalRegexp = re.compile(r'^[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+\s*\d+(\.\d*)?[-–\sa-zA-ZА-Яа-яёЁЇїІіЄєҐґ]*$')
    # float_text_regexp = re.compile(r'^.{0,12}\d+[.,]\d*.{0,9}$')
    float_text_regexp = re.compile(r'^.{0,6}\d+([.,]\d*.{0,9})*.{0,12}$')


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

    def get_ranks_for_observation(self, raw_observation):
        res_ranks_dict = {}
        for value in raw_observation:
            if value.__class__ == int or value.__class__ == float:
                res_ranks_dict[value] = value
            else:
                res_ranks_dict[str(value)] = float(re.search(f'\d+([.,]\d+)?', str(value))[0])
        return res_ranks_dict

    # def validate_interval(self, value):
    #     number_regexp = re.compile(r'(\d+(\.\d*)?)')
    #     string_numbers = list(map(lambda m: tuple(filter(bool, m))[0], re.findall(number_regexp, value)))
    #     if float(string_numbers[0]) < float(string_numbers[1]):
    #         return True
    #     else:
    #         return False
