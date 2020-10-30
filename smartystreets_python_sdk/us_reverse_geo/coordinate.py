class Coordinate:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-reverse-geo-api#coordinate"
        """
        self.latitude = obj.get('latitude', None)
        self.longitude = obj.get('longitude', None)
        self.accuracy = obj.get('accuracy', None)
        self.license = obj.get('license', None)
