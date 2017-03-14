from smartystreets_python_sdk.exceptions import UnprocessableEntityError


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

    @property
    def missing_country(self):
        return self.field_is_missing(self.country)

    @property
    def has_freeform(self):
        return self.field_is_set(self.freeform)

    @property
    def missing_address1(self):
        return self.field_is_missing(self.address1)

    @property
    def has_postal_code(self):
        return self.field_is_set(self.postal_code)

    @property
    def missing_locality_or_administrative_area(self):
        return self.field_is_missing(self.locality) or self.field_is_missing(self.administrative_area)

    @staticmethod
    def field_is_missing(field):
        return field is None or field == ''

    def field_is_set(self, field):
        return not self.field_is_missing(field)

    def ensure_enough_info(self):
        if self.missing_country:
            raise UnprocessableEntityError('Country field is required.')

        if self.has_freeform:
            return True

        if self.missing_address1:
            raise UnprocessableEntityError('Either freeform or address1 is required.')

        if self.has_postal_code:
            return True

        if self.missing_locality_or_administrative_area:
            raise UnprocessableEntityError('Insufficient information: One or more required fields were not set on the lookup.')
