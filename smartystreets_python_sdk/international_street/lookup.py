from smartystreets_python_sdk.exceptions import UnprocessableEntityError


class Lookup:
    def __init__(self, freeform=None, country=None):
        """
        In addition to holding all of the input data for this lookup, this class also will contain the 
        result of the lookup after it comes back from the API.
        
        Note: Lookups must have certain required fields set with non-blank values.
            These can be found at the URL below.
            
        See "https://smartystreets.com/docs/cloud/international-street-api#http-input-fields"
        
        :field self.geocode: Disabled by default. Set to true to enable.
        :field self.language: When not set, the output language will match the language of the input values.
            When set to language_mode.NATIVE, the results will always be in the language of the output country.
            When set to language_mode.LATIN, the results will always be provided using a Latin character set.
        """
        self.result = []

        self.input_id = None
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
