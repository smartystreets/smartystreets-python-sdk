class Suggestion:
    def __init__(self, obj=None):
        self.text = obj.get('text', None)
        self.street_line = obj.get('street_line', None)
        self.city = obj.get('city', None)
        self.state = obj.get('state', None)
