class Lookup:
    def __init__(self, freeform=None, country=None):
        self.result = []

        self.inputId = None
        self.country = country
        self.geocode = None
        self.language = None
        self.freeform = freeform
        self.address1 = None
        self.address2 = None
        self.address3 = None
        self.address4 = None
        self.organization = None
        self.locality = None
        self.administrative_area = None
        self.postal_code = None

    def missing_country(self):
        return self.field_is_missing(self.country)

    def has_freeform(self):
        return self.field_is_set(self.freeform)

    def missing_address1(self):
        return self.field_is_missing(self.address1)

    def has_postal_code(self):
        return self.field_is_set(self.postal_code)

    def missing_locality_or_administrative_area(self):
        return self.field_is_missing(self.locality) or self.field_is_missing(self.administrative_area)

    def field_is_missing(self, field):
        return field is None or field == ''

    def field_is_set(self, field):
        return not self.field_is_missing(field)
