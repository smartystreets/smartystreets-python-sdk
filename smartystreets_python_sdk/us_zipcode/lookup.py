class Lookup:
    def __init__(self, city=None, state=None, zipcode=None, input_id=None):
        """
        In addition to holding all of the input data for this lookup, this class also
            will contain the result of the lookup after it comes back from the API.
            
            See "https://smartystreets.com/docs/cloud/us-zipcode-api#http-request-input-fields"
        """
        self.result = None
        self.custom_parameter_array = {}
        self.input_id = input_id
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def add_custom_parameter(self, parameter, value):
        self.custom_parameter_array[parameter] = value
