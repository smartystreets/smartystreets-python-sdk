import json


class NativeSerializer:
    def __init__(self):
        pass

    def serialize(self, obj):
        return json.dumps(obj).encode("UTF-8")

    def deserialize(self, payload):
        return json.loads(payload)
