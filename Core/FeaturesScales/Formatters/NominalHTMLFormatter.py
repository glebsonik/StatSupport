from Core.FeaturesScales.NominalFeature import NominalFeature


class NominalHTMLFormatter(NominalFeature):

    # def __init__(self, name, f_aggregated_data):
    #     super(NominalFeature, name, f_aggregated_data)

    @property
    def f_name(self):
        return f'<div>{self._name}</div>'

    # @name.setter
    # def name(self, name):

    @property
    def f_aggregated_data(self):
        features_list = ''
        for key in self._aggregated_data:
            features_list += '<li>' + str(key) + ' – ' + str(self._aggregated_data[key]) + '</li>\n'
        features_list = '<ul>\n' + features_list + '</ul>'
        return features_list

    def f_get_stat_info(self):
        res_html_info = ''
        info_dict = super().get_stat_info()
        for info_key in info_dict:
            res_html_info += f'<div style="font-weight:bold">{info_key}</div>'
            res_html_info += '<ul>'
            for stat_key in info_dict[info_key]:
                res_html_info += f'<li>{stat_key} – {info_dict[info_key][stat_key]}</li>'
            res_html_info += '</ul>'
        return res_html_info
