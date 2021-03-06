from Core.FeaturesScales.OrdinalFeature import OrdinalFeature


class OrdinalHTMLFormatter(OrdinalFeature):

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

    @property
    def f_ordered_data(self):
        res_ordered_data_html = ""
        for index, item in enumerate(self.ordered_data):
            res_ordered_data_html += f"<li>{index + 1} – {item} </li>"
        return f"<ul>{res_ordered_data_html}</ul>"

    def f_get_stat_info(self):
        res_html_info = ''
        info_dict = self.get_stat_info()
        for info_key in info_dict:
            res_html_info += f'<div style="font-weight:bold">{info_key}</div>'
            res_html_info += '<ul>'
            if isinstance(info_dict[info_key], dict):
                for stat_key in info_dict[info_key]:
                    res_html_info += f'<li>{stat_key} – {info_dict[info_key][stat_key]}</li>'
            else:
                res_html_info += f'<li>{info_dict[info_key]}</li>'
            res_html_info += '</ul>'
        return res_html_info

    def __str__(self):
        return(f'<div style="font-weight: bold; font-size: 20px">Feature </div>{self.f_name}'
               f'<div>Scale: <span style="font-style: italic">{self.scale}</span></div>'
               f'<div>Ranks:</div>'
               f'{self.f_ordered_data}'
               f'<div>Observation aggregated data</div>'
               f'{self.f_aggregated_data}')
