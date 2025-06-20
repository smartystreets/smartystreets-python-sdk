class Address:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#address"
        """
        self.street = obj.get('street', None)
        self.city = obj.get('city', None)
        self.state_abbreviation = obj.get('state_abbreviation', None)
        self.zipcode = obj.get('zipcode', None)
        self.source = obj.get('source', None)
        self.smartykey = obj.get('smarty_key', None)
