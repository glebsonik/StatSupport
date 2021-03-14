
class NominalCalculator:

    @staticmethod
    def calc_mode(sign_dict):
        return {k: v for (k, v) in sign_dict.items() if v == max(sign_dict.values())}
