class Metadata:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-extract-api#http-response-status"
        """
        self.lines = obj.get('lines', None)
        self.unicode = obj.get('unicode', None)
        self.address_count = obj.get('address_count', None)
        self.verified_count = obj.get('verified_count', None)
        self.bytes = obj.get('bytes', None)
        self.character_count = obj.get('character_count', None)
