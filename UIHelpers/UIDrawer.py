import copy
import matplotlib.pyplot as plt
from IPython.core.display import display, HTML
from StatsCharacteristicsBuilders import OrdinalMeasureCalculator
from StatsCharacteristicsBuilders import NominalMeasureCalculator
from StatsCharacteristicsBuilders import IntervalMeasureCalculator


class UIDrawer:

    measure_manager = None

    nominal_calc = NominalMeasureCalculator.NominalMeasureCalculator()
    ordinal_calc = OrdinalMeasureCalculator.OrdinalMeasureCalculator()
    interval_calc = IntervalMeasureCalculator.IntervalMeasureCalculator()

    def __init__(self, measure_manager):
        self.measure_manager = measure_manager

    def display_signs(self):
        aggregated_signs = self.measure_manager.get_aggregated_signs(True)
        for sign in aggregated_signs:
            print(aggregated_signs[sign])

    def display_sign(self, sign_name):
        aggregated_signs = self.measure_manager.get_aggregated_signs(True)
        if aggregated_signs[sign_name]['type'] == 'Nominal':
            self.display_info_for_nominal(sign_name)
        elif aggregated_signs[sign_name]['type'] == 'Ordinal':
            self.display_info_for_ordinal(sign_name)
        else:
            self.display_info_for_interval(sign_name)

    def display_info_for_nominal(self, sign_name):
        mode_string = self.mode_html_prettify(self.nominal_calc.calc_mode(self.measure_manager[sign_name]))
        display(HTML(f'<h2> Мода: {mode_string} </h1>'))
        self.draw_plot(sign_name, "blue")

    def display_info_for_ordinal(self, sign_name):
        mode_string = self.mode_html_prettify(self.ordinal_calc.calc_mode(self.measure_manager[sign_name]))
        display(HTML(f'<h2> Мода: {mode_string} </h1>'))

        # median_value = self.nominal_calc.calc_median(self.measure_manager.get_encoded_sign(sign_name).median())
        # display(HTML(f'<h2> Mode: {median_value} </h1>'))
        # min/max
        self.draw_plot(sign_name, "orange")

    def display_info_for_interval(self, sign_name):
        mode_string = self.mode_html_prettify(self.interval_calc.calc_mode(self.measure_manager[sign_name]))
        display(HTML(f'<h2> Мода: {mode_string} </h1>'))
        self.draw_plot(sign_name, "cyan")
        # raise NotImplemented("No implementation for rank measure")

    def draw_plot(self, sign_name, color='orange'):
        aggregated_sign_info = self.measure_manager.get_aggregated_signs()[sign_name]

        plt.figure(figsize=(35, 14))
        plt.rcParams.update({'font.size': 27})
        return plt.bar(list(aggregated_sign_info.keys()), aggregated_sign_info.values(), color=color)

    @staticmethod
    def mode_html_prettify(mode_array):
        return "".join(map(lambda x: x + "\n", mode_array)).strip().replace("\n", "<br>")