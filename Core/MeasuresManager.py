import copy
from Core.Identifiers.MeasurementDefiner import MeasurementDefiner
from Core.SignFactory import SignFactory


class MeasuresManager:

    raw_df = None
    measure_definer = MeasurementDefiner()

    def __init__(self, dtf):
        self.signs = []
        self.raw_df = copy.deepcopy(dtf)
        self.measure_format = 'html'
        self.__define_measures()

    def __dict_with_measures(self):
        data_signs = dict()
        for column in self.raw_df.columns:
            data_signs[column] = self.raw_df[column].value_counts().to_dict()
        return data_signs

    def __define_measures(self):
        sign_factory = SignFactory(self.measure_format)
        measures = self.__dict_with_measures()
        for sign_name in measures:
            self.signs.append(sign_factory.create_measure(sign_name,
                                                          measures[sign_name],
                                                          self.measure_definer.define_measure(measures[sign_name])))

    def raw_signs_names(self):
        return list(map(lambda sign: sign._name, self.signs))

    def signs_html(self):
        hdr = ''
        for sign in ["Name", "Value"]:
            hdr = hdr + '<th>' + sign + '</th>'

        for sign in self.signs:
            hdr = hdr + "<tr>"
            hdr = hdr + '<td>' + sign.name + '</td>'
            hdr = hdr + '<td style="text-align:left">' + str(sign.aggregated_data) + '</td>'
            hdr = hdr + "</tr>"
        return "<table>" + hdr + "</table>"

    # Syntax sugar
    def __getitem__(self, sign_name):
        return [sign for sign in self.signs if sign._name == sign_name][0]
