import copy
from Identifiers import MeasurementDefiner as md


class MeasuresManager:

    data_frame = None
    measure_definer = md.MeasurementDefiner()

    def __init__(self, dtf):
        self.data_frame = copy.deepcopy(dtf)

    # Syntax sugar
    def __getitem__(self, sign_name):
        return self.data_frame[sign_name]

    def get_aggregated_signs(self, with_measure = False):
        data_signs = dict()
        for column in self.data_frame.columns:
            data_signs[column] = self.data_frame[column].value_counts().to_dict()
        if with_measure:
            return self.define_measures(data_signs)
        else:
            return data_signs

    def define_measures(self, aggregated_signs_dict):
        signs_dict = copy.deepcopy(aggregated_signs_dict)
        for sign_name in signs_dict:
            signs_dict[sign_name]['type'] = self.measure_definer.define_measure(signs_dict[sign_name])
        return signs_dict

