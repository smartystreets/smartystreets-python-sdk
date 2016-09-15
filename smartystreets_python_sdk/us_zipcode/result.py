class Result:
    def __init__(self, obj):
        self.status = obj.get('status', None)
        self.reason = obj.get('reason', None)
        self.input_index = obj.get('input_index', None)
        self.cities = obj.get('city_states', [])
        self.zipcodes = obj.get('zipcodes', [])

        self.convert_cities()
        self.convert_zipcodes()

    def convert_cities(self):
        pass

    def convert_zipcodes(self):
        pass
