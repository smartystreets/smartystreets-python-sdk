class Metadata:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-street-api#metadata"
        """
        self.record_type = obj.get('record_type', None)
        self.zip_type = obj.get('zip_type', None)
        self.county_fips = obj.get('county_fips', None)
        self.county_name = obj.get('county_name', None)
        self.carrier_route = obj.get('carrier_route', None)
        self.congressional_district = obj.get('congressional_district', None)
        self.building_default_indicator = obj.get('building_default_indicator', None)
        self.rdi = obj.get('rdi', None)
        self.elot_sequence = obj.get('elot_sequence', None)
        self.elot_sort = obj.get('elot_sort', None)
        self.latitude = obj.get('latitude', None)
        self.longitude = obj.get('longitude', None)
        self.precision = obj.get('precision', None)
        self.time_zone = obj.get('time_zone', None)
        self.utc_offset = obj.get('utc_offset', None)
        self.obeys_dst = obj.get('dst', None)
        self.is_ews_match = obj.get('ews_match', None)
