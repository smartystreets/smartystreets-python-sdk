class Lookup:
    def __init__(self, freeform=None):
        self.result = []
        self.input_id = None
        self.street = freeform
        self.street2 = None
        self.secondary = None
        self.city = None
        self.state = None
        self.zipcode = None
        self.lastline = None
        self.addressee = None
        self.urbanization = None
        self.match = None
        self.candidates = 1
