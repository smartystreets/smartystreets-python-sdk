class RootLevel:
    def __init__(self, obj):
        self.input_id = obj.get("input_id", None)
        self.organization = obj.get("organization", None)
        self.address1 = obj.get("address1", None)
        self.address2 = obj.get("address2", None)
        self.address3 = obj.get("address3", None)
        self.address4 = obj.get("address4", None)
        self.address5 = obj.get("address5", None)
        self.address6 = obj.get("address6", None)
        self.address7 = obj.get("address7", None)
        self.address8 = obj.get("address8", None)