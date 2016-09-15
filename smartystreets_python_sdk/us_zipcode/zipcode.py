class ZipCode:
    def __init__(self, obj):
        self.zipcode = obj.get('zipcode', None)
        self.zipcode_type = obj.get('zipcode_type', None)
        self.default_city = obj.get('default_city', None)
        self.county_fips = obj.get('county_fips', None)
        self.county_name = obj.get('county_name', None)
        self.latitude = obj.get('latitude', None)
        self.longitude = obj.get('longitude', None)
        self.precision = obj.get('precision', None)
