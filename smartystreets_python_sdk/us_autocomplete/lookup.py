class Lookup:
    def __init__(self, prefix=None, suggestions=None, city_filter=None, state_filter=None, prefer=None, geolocate_type=None):
        self.result = []
        self.prefix = prefix
        self.max_suggestions = suggestions
        self.city_filter = city_filter or []
        self.state_filter = state_filter or []
        self.prefer = prefer or []
        self.geolocate_type = geolocate_type

    def add_city_filter(self, city):
        self.city_filter.append(city)

    def add_state_filter(self, state):
        self.state_filter.append(state)

    def add_prefer(self, prefer):
        self.prefer.append(prefer)
