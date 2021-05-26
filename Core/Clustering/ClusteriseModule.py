from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from copy import copy

class ClusteriseModule:

    def __init__(self, feature_1, feature_2):
        self.feature_1 = feature_1
        self.feature_2 = feature_2

    def clusterise_features(self):
        feature_1_encoded_data = self.encode_features(self.feature_1)
        feature_2_encoded_data = self.encode_features(self.feature_2)
        pairs_data = list()
        for i in range(len(feature_1_encoded_data)):
            pairs_data.append([feature_1_encoded_data[i], feature_2_encoded_data[i]])
        print(pairs_data)
        kmeans = KMeans(init='k-means++', max_iter=300, n_init=10, random_state=0).fit(pairs_data)
        self.build_plot(kmeans)

    def build_plot(self, kmeans):
        clusters_size = {}
        for cluster_label in kmeans.labels_:
            clusters_size[cluster_label] = clusters_size.get(cluster_label, 0) + 1
        for cluster_label in clusters_size:
            plt.scatter(kmeans.cluster_centers_[cluster_label][0],
                        kmeans.cluster_centers_[cluster_label][1],
                        s=clusters_size[cluster_label] * 125, c='orange', alpha=0.4, linewidth=4)
            plt.text(kmeans.cluster_centers_[cluster_label][0],
                     kmeans.cluster_centers_[cluster_label][1],
                     s=str(clusters_size[cluster_label]), horizontalalignment='center', verticalalignment='center')

        x_ticks_list = list(plt.xticks()[0])
        y_ticks_list = list(plt.yticks()[0])
        new_x_ticks = self.update_ticks_by_indexes(x_ticks_list,
                                                   list(self.feature_1.aggregated_data.keys()))
        new_y_ticks = self.update_ticks_by_indexes(y_ticks_list,
                                                   list(self.feature_2.aggregated_data.keys()))
        plt.xticks(x_ticks_list, new_x_ticks)
        plt.yticks(y_ticks_list, new_y_ticks)
        plt.xlabel(self.feature_1.name)
        plt.ylabel(self.feature_2.name)
        plt.figure(figsize=(35, 14))
        plt.show()

    def encode_features(self, feature):
        encoding_list = list(feature.aggregated_data.keys())
        feature_encoded_data = list(map(lambda x: encoding_list.index(x), feature.data))
        return feature_encoded_data

    def update_ticks_by_indexes(self, ticks_list, additional_values):
        """
        Will convert plot ticks tick_list [0.0, 0.25, 0.5, 0.75, 1.0]
        Using indexes and values in additional_values ['Some', 'Text']
        To ["0.0\nSome", 0.25, 0.5, 0.75, "1.0\nText"]
        """
        res_ticks = copy(ticks_list)
        for i in range(len(additional_values)):
            tick_replace_index = ticks_list.index(i)
            res_ticks[tick_replace_index] = f"{ticks_list[tick_replace_index]} or\n{additional_values[i]}"
        return res_ticks
