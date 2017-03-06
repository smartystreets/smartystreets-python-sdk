class Result:
    def __init__(self, obj):
        self.addresses = obj.get('addresses', [])
        self.metadata = obj.get('meta', {})
