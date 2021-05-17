import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import matplotlib.ticker as plticker


class DependencyAnalysisModule:

    def is_compatible(self, features_list: list):
        for feature in features_list:
            if feature.scale not in ['Interval', 'Ordinal']:
                return False
        return True

    def get_solution_messages(self, features_list):
        solution_messages = []
        for feature in features_list:
            if feature.scale not in ['Interval', 'Ordinal']:
                solution_messages.append(f"Convert feature: {feature.name} to Interval or Ordinal scale."
                                         f" Current scale: {feature.scale}\n")
        return solution_messages

    def generate_dependency_analysis(self, feature_1, feature_2):
        if not (self.is_compatible([feature_1, feature_2])):
            raise (Exception("Given features are not compatible"))
        feature_1_observations = self.get_feature_converted_observations(feature_1)
        feature_2_observations = self.get_feature_converted_observations(feature_2)
        if feature_1.scale == 'Interval' and feature_2.scale == 'Interval':
            pearson_res = pearsonr(feature_1_observations, feature_2_observations)
            self.build_plot(feature_1, feature_2, pearson_res)
            return pearson_res
        else:
            spearman_res = spearmanr(feature_1_observations, feature_2_observations)
            print(spearman_res)
            self.build_plot(feature_1, feature_2, spearman_res)
            return spearman_res

    def get_feature_converted_observations(self, feature):
        if feature.scale == 'Interval':
            return list(map(lambda value: feature.ordered_data[value], feature.data))
        elif feature.scale == 'Ordinal':
            return list(map(lambda value: feature.ordered_data.index(value) + 1, feature.data))
        else:
            raise Exception(f"Incorrect feature: {feature.__class__} for conversion")

    def build_plot(self, feature_1, feature_2, correlation_res):
        xloc = plticker.MultipleLocator(base=1)  # this locator puts ticks at regular intervals
        yloc = plticker.MultipleLocator(base=1)  # this locator puts ticks at regular intervals
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_major_locator(xloc)
        ax.yaxis.set_major_locator(yloc)
        ax.set_xlabel(feature_1.name)
        ax.set_ylabel(feature_2.name)
        fig.set_figwidth(5)
        fig.set_figheight(5)
        correlation_type = 1 if correlation_res[0] > 0 else -1
        plt.scatter(1, correlation_type, s=abs(correlation_res[0]) * 5000, c='red', alpha=0.4, linewidth=4)
        plt.plot([0, 4], [0, correlation_type * 4], 'k--')
        plt.xlim([0, 4])
        plt.ylim([-4, 4])
        plt.show()
