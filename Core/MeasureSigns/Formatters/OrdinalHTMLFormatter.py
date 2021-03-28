from Core.MeasureSigns.OrdinalMeasureSign import OrdinalMeasureSign


class OrdinalHTMLFormatter(OrdinalMeasureSign):

    @property
    def name(self):
        return f'<div>{self._name}</div>'

    # @name.setter
    # def name(self, name):

    @property
    def aggregated_data(self):
        signs_list = ''
        for key in self._aggregated_data:
            signs_list += '<li>' + str(key) + ' – ' + str(self._aggregated_data[key]) + '</li>\n'
        signs_list = '<ul>\n' + signs_list + '</ul>'
        return signs_list

    def get_stat_info(self):
        res_html_info = ''
        info_dict = super().get_stat_info()
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