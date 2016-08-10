class FakeSerializer:
    def __init__(self, output):
        self.output = output
        self.input = None

    def serialize(self, obj):
        self.input = obj
        return self.output

    def deserialize(self, payload):
        return None
