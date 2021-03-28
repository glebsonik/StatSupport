

class NominalCalculator:

    # {'sign_value_name': qty}
    def calc_mode(self, sign_dict):
        return {k: v for (k, v) in sign_dict.items() if v == max(sign_dict.values())}
