class Suggestion:
    def __init__(self, obj=None):
        """
        See "https://smartystreets.com/docs/cloud/us-autocomplete-api#http-response"
        """
        self.text = obj.get('text', None)
        self.street_line = obj.get('street_line', None)
        self.city = obj.get('city', None)
        self.state = obj.get('state', None)
