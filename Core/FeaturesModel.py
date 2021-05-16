import copy
from functools import reduce

from Core.Identifiers.FeatureScaleDefiner import FeatureScaleDefiner
from Core.ScaleFeaturesFactory import ScaleFeaturesFactory


class FeaturesModel:

    raw_df = None

    def __init__(self, dtf, formatter):
        self.features = []
        self.raw_df = copy.deepcopy(dtf)
        self.feature_format = formatter
        self.__define_scales()

    def __convert_to_python_types(self):
        features_data = dict()
        for column in self.raw_df.columns:
            features_data[column] = self.raw_df[column].tolist()
        return features_data

    def __define_scales(self):
        feature_sc_def = FeatureScaleDefiner()
        scale_factory = ScaleFeaturesFactory(self.feature_format)
        data = self.__convert_to_python_types()
        for feature_name in data:
            self.features.append(scale_factory.create_feature(feature_name, data[feature_name],
                                                              feature_sc_def.define_scale(data[feature_name])))

    def raw_features_names(self):
        return list(map(lambda feature: feature.name, self.features))

    def f_features_names(self):
        features_names_list = list(map(lambda features: features.f_name, self.features))
        if self.feature_format == 'html':
            return f"<ul>{reduce(lambda x, y: x+f'<li>{y}</li>', features_names_list, '')}</ul>"
        else:
            return features_names_list

    # def features_html(self):
    #     hdr = ''
    #     for feature in ["Name", "Value"]:
    #         hdr = hdr + '<th>' + feature + '</th>'
    #
    #     for feature in self.features:
    #         hdr = hdr + "<tr>"
    #         hdr = hdr + '<td>' + feature.name + '</td>'
    #         hdr = hdr + '<td style="text-align:left">' + str(feature.f_aggregated_data) + '</td>'
    #         hdr = hdr + "</tr>"
    #     return "<table>" + hdr + "</table>"

    # Syntax sugar
    def __getitem__(self, feature_name):
        matched_features = [feature for feature in self.features if feature.name == feature_name]
        if len(matched_features) == 0:
            raise NameError(f'No such feature found by: {feature_name}')
        return matched_features[0]

    def __setitem__(self, key, value):
        feature_index = -1
        for index, item in enumerate(self.features):
            if item.name == key:
                feature_index = index
                break
        if feature_index >= 0:
            self.features[feature_index] = value
        else:
            raise NameError(f'No such feature found by name: {value}')
