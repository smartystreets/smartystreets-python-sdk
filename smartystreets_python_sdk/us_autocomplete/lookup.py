class Lookup:
    def __init__(self, prefix=None, suggestions=None, city_filter=None, state_filter=None, prefer=None,
                 prefer_ratio=None, geolocate_type=None):
        """
        In addition to holding all of the input data for this lookup, this class also will contain the result 
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/us-autocomplete-api#http-request-input-fields"
        
        :param prefix: The beginning of an address (required)
        :param suggestions: Maximum number of suggestions
        :param city_filter: List of cities from which to include suggestions
        :param state_filter: List of states from which to include suggestions
        :param prefer: List of cities/states. Suggestions from the members of this list will appear first
        :param prefer_ratio: Percentage of suggestions that will be from preferred cities/states.
                                (Decimal value between 0 and 1)
        :param geolocate_type: This field corresponds to the geolocate and geolocate_precision fields in the 
                                US Autocomplete API. Use the constants in geolocation_type.py to set this field
        """
        self.result = []
        self.prefix = prefix
        self.max_suggestions = suggestions
        self.city_filter = city_filter or []
        self.state_filter = state_filter or []
        self.prefer = prefer or []
        self.prefer_ratio = prefer_ratio
        self.geolocate_type = geolocate_type

    def add_city_filter(self, city):
        self.city_filter.append(city)

    def add_state_filter(self, state):
        self.state_filter.append(state)

    def add_prefer(self, prefer):
        self.prefer.append(prefer)
