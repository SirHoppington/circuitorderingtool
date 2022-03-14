from api.virtual1 import v1_api


class Quote():
    def __init__(self, postcode, filters):
        self.postcode = postcode
        self.filters = filters

    def run(self):
        response = v1_api.get_quote(self.postcode, self.filters)
        return response