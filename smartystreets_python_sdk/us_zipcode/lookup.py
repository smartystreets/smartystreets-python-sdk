class Lookup:
    def __init__(self, city=None, state=None, zipcode=None, input_id=None):
        self.result = None
        self.input_id = input_id
        self.city = city
        self.state = state
        self.zipcode = zipcode
