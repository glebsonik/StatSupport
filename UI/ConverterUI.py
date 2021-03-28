from IPython.core.display import display, HTML, clear_output
from ipywidgets import widgets
from Core.SignFactory import SignFactory
from Core.MeasuresManager import MeasuresManager


class ConverterUI:

    def __init__(self, measures_manager: MeasuresManager):
        self.operation_data = {}
        self.measures_manager = measures_manager
        self.signs_dropdown = widgets.Dropdown(
            options=measures_manager.raw_signs_names(),
            value=None,
            description='Choose sign: ',
            disabled=False,
            style={'description_width': 'initial', 'width': '500px'},
            layout={'width': '100%'}
        )
        self.convert_container = widgets.VBox()
        self.convert_button = widgets.Button(description='Convert measure', disabled=True)
        self.convert_button.on_click(self.get_convert_button_controller())

        self.signs_dropdown.observe(self.get_signs_dropdown_controller())

    def ui(self):
        self.convert_container.children = ()
        clear_output(wait=True)
        display(self.signs_dropdown)

    def get_signs_dropdown_controller(self):
        def signs_dropdown_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self.operation_data['sign_name'] = self.measures_manager[change['new']].name
                measures = ['Nominal', 'Ordinal', 'Interval']
                chosen_sign = self.measures_manager[change['new']]
                self.ui()
                measures.remove(chosen_sign.measure)
                display(
                    HTML(
                        f"<div>Current measure: <span style='font-weight: bold;'>{chosen_sign.measure}</span></div>"))
                allowed_measures_dropdown = widgets.Dropdown(
                    options=measures,
                    value=None,
                    description=f'Change measure from <b><u>{chosen_sign.measure}</u></b> to:',
                    disabled=False,
                    style={'description_width': 'initial', 'font_size': '20px'},
                    layout={'width': '100%', 'height': '37px'}
                )
                allowed_measures_dropdown.observe(self.get_measure_dropdown_controller())
                display(allowed_measures_dropdown)
                display(self.convert_container)
                display(self.convert_button)

        return signs_dropdown_controller

    def get_measure_dropdown_controller(self):
        def measure_dropdown_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self.convert_button.disabled = not (self.is_data_correct())
                i = 0
                self.operation_data['measure'] = change['new']
                if change['new'] == 'Ordinal':
                    sign_values = self.measures_manager[self.signs_dropdown.value]._aggregated_data.keys()
                    for val in sign_values:
                        i += 1
                        ordinal_dropdown = widgets.Dropdown(value=None, description=f'{i}. ', options=sign_values)
                        ordinal_dropdown.observe(self.get_values_controller())
                        self.convert_container.children += (ordinal_dropdown,)

        return measure_dropdown_controller

    def is_data_correct(self):
        values = self.collect_values()
        print(values)
        is_uniq = (len(values) == 0) or ((len(values) > 0) and (len(values) == len(set(values))) and all((value is not None) for value in values))
        return is_uniq

    def get_values_controller(self):
        def values_controller(change):
            self.convert_button.disabled = not (self.is_data_correct())

        return values_controller

    def get_convert_button_controller(self):
        def convert_button_controller(sender=None):
            previous_measure = self.measures_manager[self.operation_data['sign_name']]
            sign_factory = SignFactory(self.measures_manager.measure_format)
            mr = sign_factory.create_measure(
                self.operation_data['sign_name'],
                previous_measure._aggregated_data,
                self.operation_data['measure'],
                self.collect_values()
            )
            self.measures_manager[self.operation_data['sign_name']] = mr
            self.ui()
            display(HTML(
                f"<div>Successfully converted {self.operation_data['sign_name']} to <b>{self.operation_data['measure']}</b></div>"))

        return convert_button_controller

    def collect_values(self):
        return [sign_value.value for sign_value in self.convert_container.children]
