class Lookup:
    def __init__(self, search=None, country=None, administrative_area=None, locality=None, postal_code=None):
        """
        In addition to holding all of the input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.

        :param country: The country where the desired address is located (required)
        :param search: The part of the address tht has already been typed (required)
        :param administrative_area: Limit the results to only the administrative area provided
        :param locality: Limit the results to only the locality provided
        :param postal_code: Limit the results to only the postal code provided
        """
        self.result = []

        self.search = search
        self.country = country
        self.administrative_area = administrative_area
        self.locality = locality
        self.postal_code = postal_code
