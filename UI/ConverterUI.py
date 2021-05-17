from ipywidgets import widgets
from IPython.core.display import HTML, clear_output
from IPython.display import display

from Core.ScaleFeaturesFactory import ScaleFeaturesFactory
from Core.FeaturesModel import FeaturesModel


class ConverterUI:

    def __init__(self, scales_manager: FeaturesModel):
        self.operation_data = {}
        self.scales_manager = scales_manager
        self.features_dropdown = widgets.Dropdown(
            options=scales_manager.raw_features_names(),
            value=None,
            description='Choose feature: ',
            disabled=False,
            style={'description_width': 'initial', 'width': '500px'},
            layout={'width': '100%'}
        )
        self.convert_container = widgets.VBox()
        self.convert_button = widgets.Button(description='Convert scale', disabled=True)
        self.convert_button.on_click(self.get_convert_button_controller())
        self.features_dropdown.observe(self.get_features_dropdown_controller())
        self.recently_changed = []

    def ui(self):
        self.convert_container.children = ()
        clear_output(wait=True)
        display(self.features_dropdown)
        if len(self.recently_changed) != 0:
            display("Recently changed: " + str(self.recently_changed))

    def get_features_dropdown_controller(self):
        def features_dropdown_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self.operation_data['feature_name'] = self.scales_manager[change['new']].name
                scales = ['Nominal', 'Ordinal', 'Interval']
                chosen_feature = self.scales_manager[change['new']]
                self.ui()
                scales.remove(chosen_feature.scale)
                display(
                    HTML(
                        f"<div>Current scale: <span style='font-weight: bold;'>{chosen_feature.scale}</span></div>"))
                allowed_scales_dropdown = widgets.Dropdown(
                    options=list(map(lambda x: (x, x.lower()), scales)),
                    value=None,
                    description=f'Change scale from <b><u>{chosen_feature.scale}</u></b> to:',
                    disabled=False,
                    style={'description_width': 'initial', 'font_size': '20px'},
                    layout={'width': '100%', 'height': '37px'}
                )
                allowed_scales_dropdown.observe(self.get_scale_dropdown_controller())
                display(allowed_scales_dropdown)
                display(self.convert_container)
                self.convert_button.disabled = not (self.is_data_correct())
                display(self.convert_button)

        return features_dropdown_controller

    def get_scale_dropdown_controller(self):
        def scale_dropdown_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self.convert_container.children = ()
                self.operation_data['scale'] = change['new']
                i = 0
                if change['new'] == 'ordinal':
                    feature_values = self.scales_manager[self.features_dropdown.value].aggregated_data.keys()
                    for _ in feature_values:
                        i += 1
                        ordinal_dropdown = widgets.Dropdown(value=None, description=f'{i}. ', options=feature_values)
                        ordinal_dropdown.observe(self.get_values_controller())
                        self.convert_container.children += (ordinal_dropdown,)
                elif change['new'] == 'interval':
                    feature_values = self.scales_manager[self.features_dropdown.value].aggregated_data.keys()
                    for val in feature_values:
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

        return scale_dropdown_controller

    def is_data_correct(self):
        values = self.collect_values()
        is_nominal_correct = ((len(values) == 0) and self.operation_data.get('scale', '') == 'nominal')
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
            getattr(self, f"create_{self.operation_data['scale']}_scale")()
            self.recently_changed.append(self.operation_data['feature_name'])
            self.ui()
            display(HTML(
                f"<div>Successfully converted {self.operation_data['feature_name']} to <b>{self.operation_data['scale']}</b></div>"))
            self.operation_data = {}
        return convert_button_controller

    def create_nominal_scale(self):
        previous_scale = self.scales_manager[self.operation_data['feature_name']]
        feature_factory = ScaleFeaturesFactory(self.scales_manager.feature_format)
        new_scale = feature_factory.create_feature(self.operation_data['feature_name'], previous_scale.data,
                                                   self.operation_data['scale'])
        self.scales_manager[self.operation_data['feature_name']] = new_scale

    def create_ordinal_scale(self):
        previous_scale = self.scales_manager[self.operation_data['feature_name']]
        feature_factory = ScaleFeaturesFactory(self.scales_manager.feature_format)
        new_scale = feature_factory.create_feature(self.operation_data['feature_name'], previous_scale.data,
                                                   self.operation_data['scale'], self.collect_values())
        self.scales_manager[self.operation_data['feature_name']] = new_scale

    def create_interval_scale(self):
        previous_scale = self.scales_manager[self.operation_data['feature_name']]
        feature_factory = ScaleFeaturesFactory(self.scales_manager.feature_format)
        values_weights = self.collect_values()
        value_names = list(previous_scale.aggregated_data.keys())
        values_dict = {}
        for i in range(len(values_weights)):
            values_dict[value_names[i]] = values_weights[i]
        new_scale = feature_factory.create_feature(self.operation_data['feature_name'], previous_scale.data,
                                                   self.operation_data['scale'], values_dict)
        self.scales_manager[self.operation_data['feature_name']] = new_scale

    def collect_values(self):
        return [feature_value.value for feature_value in self.convert_container.children]
