from .alternate_county import AlternateCounty


class ZipCode:
    def __init__(self, obj: dict) -> None:
        """
        See "https://smartystreets.com/docs/cloud/us-zipcode-api#zipcodes"
        """
        self.zipcode: str | None = obj.get('zipcode')
        self.zipcode_type: str | None = obj.get('zipcode_type')
        self.default_city: str | None = obj.get('default_city')
        self.county_fips: str | None = obj.get('county_fips')
        self.county_name: str | None = obj.get('county_name')
        self.state_abbreviation: str | None = obj.get('state_abbreviation')
        self.state: str | None = obj.get('state')
        self.latitude: float | None = obj.get('latitude')
        self.longitude: float | None = obj.get('longitude')
        self.precision: str | None = obj.get('precision')
        alternate_counties = obj.get('alternate_counties', [])

        self.alternate_counties: list[AlternateCounty] = [AlternateCounty(alternate_county) for alternate_county in alternate_counties]
