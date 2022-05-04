class Lookup:
    def __init__(self, latitude=None, longitude=None):
        """
        In addition to holding the lat/lon data for this lookup, this class also will contain the
        result of the lookup after it comes back from the API.

        See https://smartystreets.com/docs/cloud/us-reverse-geo-api#http-input-fields
        """
        self.results = []

        self.latitude = round(latitude, 8)
        self.longitude = round(longitude, 8)
