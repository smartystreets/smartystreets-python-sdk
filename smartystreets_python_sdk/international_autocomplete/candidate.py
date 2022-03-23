class Candidate:
    def __init__(self, obj=None):
        self.street = obj.get('street', None)
        self.locality = obj.get('locality', None)
        self.administrative_area = obj.get('administrative_area', None)
        self.postal_code = obj.get('postal_code', None)
        self.country_iso3 = obj.get('country_iso3', None)
