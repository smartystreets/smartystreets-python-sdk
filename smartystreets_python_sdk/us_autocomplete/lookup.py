class Lookup:
    def __init__(self, prefix=None, suggestions=None, city_filter=[], state_filter=[], prefer=[], geolocate_type=None):
        self.result = []
        self.prefix = prefix
        self.max_suggestions = suggestions
        self.city_filter = city_filter
        self.state_filter = state_filter
        self.prefer = prefer
        self.geolocate_type = geolocate_type

    def add_city_filter(self, city):
        self.city_filter.append(city)

    def add_state_filter(self, state):
        self.state_filter.append(state)

    def add_prefer(self, prefer):
        self.prefer.append(prefer)
