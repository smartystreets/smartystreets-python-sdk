class Lookup:
    def __init__(self, prefix=None, suggestions=None, city_filter=None, state_filter=None, prefer=None, geolocate_type=None):
        self.result = []
        self.prefix = prefix
        self.suggestions = suggestions
        self.city_filter = city_filter
        self.state_filter = state_filter
        self.prefer = prefer
        self.geolocate_type = geolocate_type
