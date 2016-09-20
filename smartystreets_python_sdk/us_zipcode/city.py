class City:
    def __init__(self, obj):
        self.city = obj.get('city')
        self.mailable_city = obj.get('mailable_city')
        self.state_abbreviation = obj.get('state_abbreviation')
        self.state = obj.get('state')
