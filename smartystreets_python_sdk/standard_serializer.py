import json


class StandardSerializer:
    def __init__(self):
        pass

    def serialize(self, obj):
        converted_obj = []
        for item in obj:
            converted_obj.append(item.__dict__)

        return json.dumps(converted_obj).encode("UTF-8")

    def deserialize(self, payload):
        return json.loads(payload)
