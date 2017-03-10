class Metadata:
    def __init__(self, obj):
        self.latitude = obj.get('latitude', None)
        self.longitude = obj.get('longitude', None)
        self.geocode_precision = obj.get('geocode_precision', None)
        self.max_geocode_precision = obj.get('max_geocode_precision', None)
