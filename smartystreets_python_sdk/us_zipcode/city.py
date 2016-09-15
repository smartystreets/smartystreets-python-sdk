class City:
    def __init__(self, obj):
        self.city = obj.get('city', None)
        self.mailable_city = obj.get('mailable_city', None)
        self.state_abbreviation = obj.get('state_abbreviation', None)
        self.state = obj.get('state', None)
