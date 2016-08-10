class FakeDeserializer:
    def __init__(self, output):
        self.output = output
        self.input = None

    def serialize(self, obj):
        return ""

    def deserialize(self, body):
        self.input = body
        return self.output
