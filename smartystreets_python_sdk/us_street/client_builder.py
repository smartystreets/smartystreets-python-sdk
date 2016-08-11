import smartystreets_python_sdk as smarty
from smartystreets_python_sdk.us_street import Client


class ClientBuilder:
    def __init__(self, signer):
        self.signer = signer
        self.serializer = smarty.RequestsSerializer()
        self.http_sender = None
        self.maxretries = 5
        self.maxtimeout = 10000
        self.urlprefix = "https://api.smartystreets.com/street-address"

    def retry_at_most(self, maxretries):
        self.maxretries = maxretries
        return self

    def with_max_timeout(self, maxtimeout):
        self.maxtimeout = maxtimeout
        return self

    def with_serializer(self, serializer):
        self.serializer = serializer
        return self

    def with_url(self, urlprefix):
        self.urlprefix = urlprefix
        return self

    def build(self):
        return Client(self.urlprefix, self.buildsender(), self.serializer)

    def buildsender(self):
        # TODO: Implement this
        pass
