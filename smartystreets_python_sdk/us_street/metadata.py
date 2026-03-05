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
        self.coordinate_license = obj.get('coordinate_license', None)
        self.precision = obj.get('precision', None)
        self.time_zone = obj.get('time_zone', None)
        self.utc_offset = obj.get('utc_offset', None)
        self.obeys_dst = obj.get('dst', None)
        self.iana_time_zone = obj.get('iana_time_zone', None)
        self.iana_utc_offset = obj.get('iana_utc_offset', None)
        self.iana_obeys_dst = obj.get('iana_dst', None)
        self.is_ews_match = obj.get('ews_match', None)

    def to_dict(self):
        result = {
            "record_type": self.record_type,
            "zip_type": self.zip_type,
            "county_fips": self.county_fips,
            "county_name": self.county_name,
            "carrier_route": self.carrier_route,
            "congressional_district": self.congressional_district,
            "building_default_indicator": self.building_default_indicator,
            "rdi": self.rdi,
            "elot_sequence": self.elot_sequence,
            "elot_sort": self.elot_sort,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "coordinate_license": self.coordinate_license,
            "precision": self.precision,
            "time_zone": self.time_zone,
            "utc_offset": self.utc_offset,
            "dst": self.obeys_dst,
            "ews_match": self.is_ews_match
        }
        return {k: v for k, v in result.items() if v is not None}