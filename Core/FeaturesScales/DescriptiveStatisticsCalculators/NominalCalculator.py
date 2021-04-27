class NominalCalculator:

    # {'feature_value_name': qty}
    def calc_mode(self, feature_dict):
        return {k: v for (k, v) in feature_dict.items() if v == max(feature_dict.values())}
