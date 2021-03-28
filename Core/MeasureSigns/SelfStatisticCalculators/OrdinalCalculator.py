from .NominalCalculator import NominalCalculator


class OrdinalCalculator(NominalCalculator):

    def calc_median(self, order_signs_data: list, aggregated_data: dict):
        if len(order_signs_data) % 2 != 0:
            value_name = order_signs_data[int((len(order_signs_data) + 1) / 2) - 1]
            return {value_name: aggregated_data[value_name]}
        else:
            return None

    def calc_range(self, signs_data: list):
        return len(signs_data) - 1

    def calc_min(self, encoded_sign_dict):
        raise NotImplemented("Method is not implemented")

    def calc_max(self, encoded_sign_dict):
        raise NotImplemented("Method is not implemented")
