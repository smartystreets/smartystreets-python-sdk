class AlternateCounty:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-zipcode-api#zipcodes"
        """
        self.county_fips = obj.get('county_fips')
        self.county_name = obj.get('county_name')
        self.state_abbreviation = obj.get('state_abbreviation')
        self.state = obj.get('state')
