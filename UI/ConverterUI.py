from ipywidgets import widgets
from IPython.core.display import HTML, clear_output
from IPython.display import display

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
                    options=list(map(lambda x: (x, x.lower()), measures)),
                    value=None,
                    description=f'Change measure from <b><u>{chosen_sign.measure}</u></b> to:',
                    disabled=False,
                    style={'description_width': 'initial', 'font_size': '20px'},
                    layout={'width': '100%', 'height': '37px'}
                )
                allowed_measures_dropdown.observe(self.get_measure_dropdown_controller())
                display(allowed_measures_dropdown)
                display(self.convert_container)
                self.convert_button.disabled = not (self.is_data_correct())
                display(self.convert_button)

        return signs_dropdown_controller

    def get_measure_dropdown_controller(self):
        def measure_dropdown_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self.convert_container.children = ()
                self.operation_data['measure'] = change['new']
                i = 0
                if change['new'] == 'ordinal':
                    sign_values = self.measures_manager[self.signs_dropdown.value].aggregated_data.keys()
                    for _ in sign_values:
                        i += 1
                        ordinal_dropdown = widgets.Dropdown(value=None, description=f'{i}. ', options=sign_values)
                        ordinal_dropdown.observe(self.get_values_controller())
                        self.convert_container.children += (ordinal_dropdown,)
                elif change['new'] == 'interval':
                    sign_values = self.measures_manager[self.signs_dropdown.value].aggregated_data.keys()
                    for val in sign_values:
                        i += 1
                        interval_dropdown = widgets.FloatText(
                            value=1.0 + round(i / 10, 1),
                            step=0.1,
                            description=f'{val} :',
                            disabled=False,
                            style={'description_width': '50%'},
                        )
                        interval_dropdown.observe(self.get_values_controller())
                        self.convert_container.children += (interval_dropdown,)
                self.convert_button.disabled = not (self.is_data_correct())

        return measure_dropdown_controller

    def is_data_correct(self):
        values = self.collect_values()
        is_nominal_correct = ((len(values) == 0) and self.operation_data.get('measure', '') == 'nominal')
        is_selectors_data_correct = all((value is not None) for value in values)

        is_ord_int_correct = ((len(values) > 0) and (len(values) == len(set(values))) and is_selectors_data_correct)
        is_uniq = is_nominal_correct or is_ord_int_correct
        return is_uniq

    def get_values_controller(self):
        def values_controller(change):
            self.convert_button.disabled = not (self.is_data_correct())
        return values_controller

    def get_convert_button_controller(self):
        def convert_button_controller(sender):
            getattr(self, f"create_{self.operation_data['measure']}_measure")()
            self.ui()
            display(HTML(
                f"<div>Successfully converted {self.operation_data['sign_name']} to <b>{self.operation_data['measure']}</b></div>"))
            self.operation_data = {}
        return convert_button_controller

    def create_nominal_measure(self):
        previous_measure = self.measures_manager[self.operation_data['sign_name']]
        sign_factory = SignFactory(self.measures_manager.measure_format)
        new_measure = sign_factory.create_measure(
            self.operation_data['sign_name'],
            previous_measure.aggregated_data,
            self.operation_data['measure']
        )
        self.measures_manager[self.operation_data['sign_name']] = new_measure

    def create_ordinal_measure(self):
        previous_measure = self.measures_manager[self.operation_data['sign_name']]
        sign_factory = SignFactory(self.measures_manager.measure_format)
        new_measure = sign_factory.create_measure(
            self.operation_data['sign_name'],
            previous_measure.aggregated_data,
            self.operation_data['measure'],
            self.collect_values()
        )
        self.measures_manager[self.operation_data['sign_name']] = new_measure

    def create_interval_measure(self):
        previous_measure = self.measures_manager[self.operation_data['sign_name']]
        sign_factory = SignFactory(self.measures_manager.measure_format)
        values_weights = self.collect_values()
        value_names = list(previous_measure.aggregated_data.keys())
        values_dict = {}
        for i in range(len(values_weights)):
            values_dict[value_names[i]] = values_weights[i]
        print('values dict: ', values_dict)
        new_measure = sign_factory.create_measure(
            self.operation_data['sign_name'],
            previous_measure.aggregated_data,
            self.operation_data['measure'],
            values_dict
        )
        print('new meas', new_measure)
        print('sign name', self.operation_data['sign_name'])
        self.measures_manager[self.operation_data['sign_name']] = new_measure

    def collect_values(self):
        return [sign_value.value for sign_value in self.convert_container.children]
