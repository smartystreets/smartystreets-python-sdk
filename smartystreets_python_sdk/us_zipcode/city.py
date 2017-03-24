class City:
    def __init__(self, obj):
        """
        Known in the SmartyStreets US ZIP Code API documentation as a city_state
        See "https://smartystreets.com/docs/cloud/us-zipcode-api#cities"
        """
        self.city = obj.get('city')
        self.mailable_city = obj.get('mailable_city')
        self.state_abbreviation = obj.get('state_abbreviation')
        self.state = obj.get('state')
