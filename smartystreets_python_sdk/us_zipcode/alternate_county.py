class AlternateCounty:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-zipcode-api#zipcodes"
        """
        self.county_fips: str | None = obj.get('county_fips')
        self.county_name: str | None = obj.get('county_name')
        self.state_abbreviation: str | None = obj.get('state_abbreviation')
        self.state: str | None = obj.get('state')
