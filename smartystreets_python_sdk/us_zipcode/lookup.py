from smartystreets_python_sdk.us_zipcode import Result


class Lookup:
    def __init__(self, city=None, state=None, zipcode=None):
        self.result = Result()
        self.input_id = None
        self.city = city
        self.state = state
        self.zipcode = zipcode
