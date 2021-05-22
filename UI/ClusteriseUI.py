from ipywidgets import widgets
from IPython.core.display import HTML, clear_output
from IPython.display import display
from functools import reduce

from Core.FeaturesModel import FeaturesModel
from Core.DependencyAnalysis.DependencyAnalysisModule import DependencyAnalysisModule
from Core.Clustering.ClusteriseModule import ClusteriseModule

class ClusteriseUI:

    def __init__(self, features_model: FeaturesModel):
        self._feature_1 = None
        self._feature_2 = None
        self._features_model = features_model

    def ui(self):
        feature_1_dropdown = widgets.Dropdown(
            options=self._features_model.raw_features_names(),
            value=None,
            description='Choose feature 1: ',
            style={'description_width': 'initial'},
            layout={'width': '100%'}
        )
        feature_1_dropdown.observe(self._get_dropdown_controller_1())
        display(feature_1_dropdown)

    def _get_dropdown_controller_1(self):
        def dropdown_controller_1(change):
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
        return dropdown_controller_1

    def _get_dropdown_2_controller(self):
        def dropdown_2_controller(change):
            if change['type'] == 'change' and change['name'] == 'value':
                self._feature_2 = self._features_model[change['new']]
                clear_output()
                ClusteriseModule(self._feature_1, self._feature_2).clusterise_features()
                self.ui()
        return dropdown_2_controller
