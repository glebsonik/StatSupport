class DataAggregator:

    @staticmethod
    def aggregate_list(list_of_values: list):
        aggregated_dict = {}
        for value_name in list_of_values:
            aggregated_dict[value_name] = aggregated_dict.get(value_name, 0) + 1
        return aggregated_dict
