class ZipCode:
    def __init__(self, obj):
        self.zipcode = obj.get('zipcode')
        self.zipcode_type = obj.get('zipcode_type')
        self.default_city = obj.get('default_city')
        self.county_fips = obj.get('county_fips')
        self.county_name = obj.get('county_name')
        self.latitude = obj.get('latitude')
        self.longitude = obj.get('longitude')
        self.precision = obj.get('precision')
