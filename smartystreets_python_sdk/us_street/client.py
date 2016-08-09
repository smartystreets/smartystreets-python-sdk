from smartystreets_python_sdk.us_street import Batch


class Client:
    def __init__(self, urlprefix, sender, serializer):
        self.urlprefix = urlprefix
        self.sender = sender
        self.serializer = serializer

    def send_lookup(self, lookup):
        batch = Batch()
        batch.add(lookup)
        self.send_batch()

    def send_batch(self):
        pass
