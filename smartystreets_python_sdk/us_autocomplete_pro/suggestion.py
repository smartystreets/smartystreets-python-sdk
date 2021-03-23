class Suggestion:
    def __init__(self, obj=None):
        """
        See "https://smartystreets.com/docs/cloud/us-autocomplete-api#http-response"
        """
        self.street_line = obj.get('street_line', None)
        self.secondary = obj.get('secondary', None)
        self.city = obj.get('city', None)
        self.state = obj.get('state', None)
        self.zipcode = obj.get('zipcode', None)
        self.entries = obj.get('entries', None)
