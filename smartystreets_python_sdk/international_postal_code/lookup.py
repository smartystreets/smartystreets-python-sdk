class Lookup:
    def __init__(self):
        """
        In addition to holding all the input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/international-postal-code-api"
        """
        self.results = []
        
        self.input_id = None
        self.country = None
        self.locality = None
        self.administrative_area = None
        self.postal_code = None

    def populate(self, params):
        if self.input_id:
            params['input_id'] = self.input_id
        if self.country:
            params['country'] = self.country
        if self.locality:
            params['locality'] = self.locality
        if self.administrative_area:
            params['administrative_area'] = self.administrative_area
        if self.postal_code:
            params['postal_code'] = self.postal_code
