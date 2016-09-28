import smartystreets_python_sdk as smarty
from .client import Client


class ClientBuilder:
    def __init__(self, signer):
        self.signer = signer
        self.serializer = smarty.StandardSerializer()
        self.http_sender = None
        self.max_retries = 5
        self.max_timeout = 10000
        self.url_prefix = "https://us-zipcode.api.smartystreets.com/lookup"

    def retry_at_most(self, max_retries):
        self.max_retries = max_retries
        return self

    def with_max_timeout(self, max_timeout):
        self.max_timeout = max_timeout
        return self

    def with_serializer(self, serializer):
        self.serializer = serializer
        return self

    def with_url(self, url_prefix):
        self.url_prefix = url_prefix
        return self

    def build(self):
        return Client(self.build_sender(), self.serializer)

    def build_sender(self):
        if self.http_sender is not None:
            return self.http_sender

        sender = smarty.RequestsSender(self.max_timeout)

        sender = smarty.StatusCodeSender(sender)

        if self.signer is not None:
            sender = smarty.SigningSender(self.signer, sender)

        if self.max_retries > 0:
            sender = smarty.RetrySender(self.max_retries, sender)

        sender = smarty.URLPrefixSender(self.url_prefix, sender)

        return sender
