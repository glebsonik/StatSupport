class OrdinalIdentifier:

    def is_ordinal(self, data_sign):
        return len(list(data_sign.keys())) >= 3
