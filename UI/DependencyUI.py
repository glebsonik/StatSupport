from ipywidgets import widgets
from IPython.core.display import HTML, clear_output
from IPython.display import display

from Core.FeaturesModel import FeaturesModel
from Core.DependencyAnalysis.DependencyAnalysisModule import DependencyAnalysisModule
from functools import reduce

class DependencyUI:
    def __init__(self, features_model: FeaturesModel):
        self._feature_1 = None
        self._feature_2 = None
        self._features_model = features_model

    def ui(self):
        feature_1_dropdown = widgets.Dropdown(
            options=self._features_model.raw_features_names(),
            value=None,
            description='Choose feature: ',
            style={'description_width': 'initial'},
            layout={'width': '100%'}
        )
        feature_1_dropdown.observe(self._get_dropdown_1_controller())
        display(feature_1_dropdown)

    def _get_dropdown_1_controller(self):
        def dropdown_1_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self._feature_1 = self._features_model[change['new']]
                allowed_features_names = list(filter(lambda x: x != self._feature_1.name,
                                                     self._features_model.raw_features_names()))
                feature_2_dropdown = widgets.Dropdown(
                    options=allowed_features_names,
                    value=None,
                    description='Choose feature 2: ',
                    style={'description_width': 'initial'},
                    layout={'width': '100%'}
                )
                feature_2_dropdown.observe(self._get_dropdown_2_controller())
                display(feature_2_dropdown)
        return dropdown_1_controller

    def _get_dropdown_2_controller(self):
        def dropdown_2_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self._feature_2 = self._features_model[change['new']]
                dependency_module = DependencyAnalysisModule()
                if dependency_module.is_compatible([self._feature_1, self._feature_2]):
                    clear_output()
                    dependency_index, non_correlation = dependency_module.generate_dependency_analysis(self._feature_1,
                                                                                                       self._feature_2)
                    display(HTML(f"<div>Dependency correlation index: "
                                    f"<span style='font-weight:bold;'>{dependency_index}</span></div>"
                                 f"Probability that data is not correlated: "
                                    f"<span style='font-weight:bold;'>{non_correlation}</span>"
                                 f"</div>"))
                    self.ui()
                else:
                    clear_output()
                    solution_messages = dependency_module.get_solution_messages([self._feature_1, self._feature_2])
                    format_message = reduce(lambda x, y: x + f"<div>{y}<hr></div>", solution_messages, '')
                    display(HTML(f"<div>"
                                 f"Features: "
                                 f"<div style='font-weight:bold'><b>{self._feature_1.name}</b></div>"
                                 f"and"
                                 f"<div style='font-weight:bold'><b>{self._feature_2.name}</b></div>"
                                 f"Advices: {format_message}"
                                 f"</div>"))
                    self.ui()
        return dropdown_2_controller
