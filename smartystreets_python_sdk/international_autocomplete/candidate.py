class Candidate:
    def __init__(self, obj=None):
        self.street = obj.get('street', None)
        self.locality = obj.get('locality', None)
        self.administrative_area = obj.get('administrative_area', None)
        self.administrative_area_short = obj.get('administrative_area_short', None)
        self.administrative_area_long = obj.get('administrative_area_long', None)
        self.postal_code = obj.get('postal_code', None)
        self.country_iso3 = obj.get('country_iso3', None)
        # v2 fields
        self.entries = obj.get('entries', None)
        self.address_text = obj.get('address_text', None)
        self.address_id = obj.get('address_id', None)
