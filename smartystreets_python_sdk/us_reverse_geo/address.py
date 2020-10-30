class Address:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#address"
        """
        self.street = obj.get('street', None)
        self.city = obj.get('city', None)
        self.state_abbreviation = obj.get('state_abbreviation', None)
        self.zipcode = obj.get('zipcode', None)
