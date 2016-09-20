class Lookup:
    def __init__(self, street=None, street2=None, secondary=None, city=None, state=None, zipcode=None, lastline=None,
                 addressee=None, urbanization=None, match=None, candidates=1, input_id=None):
        self.result = []
        self.input_id = input_id
        self.street = street
        self.street2 = street2
        self.secondary = secondary
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.lastline = lastline
        self.addressee = addressee
        self.urbanization = urbanization
        self.match = match
        self.candidates = candidates
