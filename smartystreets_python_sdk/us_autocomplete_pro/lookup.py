from smartystreets_python_sdk.us_autocomplete_pro import geolocation_type


class Lookup:
    def __init__(self, search=None, max_results=None, city_filter=None, state_filter=None, zip_filter=None,
                 exclude=None, prefer_cities=None, prefer_states=None, prefer_zips=None, prefer_ratio=None,
                 prefer_geo=None, selected=None, source=None):

        """
        In addition to holding all of the input data for this lookup, this class also will contain the result 
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/us-autocomplete-api#http-request-input-fields"

        :param search: The part of the address that has already been typed (required)
        :param max_results: Maximum number of address suggestions to return
        :param city_filter: Limit the results to only those cities listed, as well as those in state_filter
        :param state_filter: Limit the results to only those states listed, as well as those in city_filter
        :param zip_filter: Limit the result to only those ZIP Codes listed. When this parameter is used,
                            no other _cities, _states parameters can be used
        :param exclude: Exclude the following states from the results. When this parameter is used,
                            no other include_ parameters can be used
        :param prefer_cities: Display suggestions with the listed cities and states at the top of the suggestion list
        :param prefer_states: Display suggestions with the listed states at the top of the suggestion list
        :param prefer_zips: Display suggestions with the listed ZIP Codes at the top of the suggestion list.
                                When this parameter is used, no other _cities or _state parameters can be used
        :param prefer_ratio: Specifies the percentage of address suggestions that should be preferred
                                and will appear at the top of the suggestion list
        :param prefer_geo: If omitted or set to city it uses the sender's IP address to determine location,
                            then automatically adds the city and state to the prefer_cities value.
                            This parameter takes precedence over other _include or exclude parameters,
                            meaning that if it is not set to none, you may see addresses from the customer's area
                            when you may not desire it
        :param selected: Used by UI components to request a list of secondaries (up to 100) for the specified address
        """
        self.result = []
        self.search = search
        self.max_results = max_results
        self.city_filter = city_filter or []
        self.state_filter = state_filter or []
        self.zip_filter = zip_filter or []
        self.exclude = exclude or []
        self.prefer_cities = prefer_cities or []
        self.prefer_states = prefer_states or []
        self.prefer_zips = prefer_zips or []
        self.prefer_ratio = prefer_ratio
        self.prefer_geo = prefer_geo
        self.selected = selected
        self.source = source

    def add_city_filter(self, city):
        self.city_filter.append(city)

    def add_state_filter(self, state):
        self.state_filter.append(state)

    def add_zip_filter(self, zipcode):
        self.prefer_geo = geolocation_type.NONE
        self.zip_filter.append(zipcode)

    def add_exclude(self, state):
        self.exclude.append(state)

    def add_city_preference(self, city):
        self.prefer_cities.append(city)

    def add_state_preference(self, state):
        self.prefer_states.append(state)

    def add_zip_preference(self, zipcode):
        self.prefer_geo = geolocation_type.NONE
        self.prefer_zips.append(zipcode)
