import smartystreets_python_sdk as smarty
from smartystreets_python_sdk.us_street import Client as USStreetClient
from smartystreets_python_sdk.us_zipcode import Client as USZIPClient
from smartystreets_python_sdk.us_extract import Client as USExtractClient
from smartystreets_python_sdk.us_autocomplete import Client as USAutocompleteClient
from smartystreets_python_sdk.international_street import Client as InternationalStreetClient


class ClientBuilder:
    def __init__(self, signer):
        self.signer = signer
        self.serializer = smarty.NativeSerializer()
        self.http_sender = None
        self.max_retries = 5
        self.max_timeout = 10000
        self.url_prefix = None
        self.INTERNATIONAL_STREET_API_URL = "https://international-street.api.smartystreets.com/verify"
        self.US_AUTOCOMPLETE_API_URL = "https://us-autocomplete.api.smartystreets.com/suggest"
        self.US_EXTRACT_API_URL = "https://us-extract.api.smartystreets.com"
        self.US_STREET_API_URL = "https://us-street.api.smartystreets.com/street-address"
        self.US_ZIP_CODE_API_URL = "https://us-zipcode.api.smartystreets.com/lookup"

    def retry_at_most(self, max_retries):
        self.max_retries = max_retries
        return self

    def with_max_timeout(self, max_timeout):
        self.max_timeout = max_timeout
        return self

    def with_sender(self, sender):
        self.http_sender = sender
        return self

    def with_serializer(self, serializer):
        self.serializer = serializer
        return self

    def with_base_url(self, url_prefix):
        self.url_prefix = url_prefix
        return self

    def build_international_street_api_client(self):
        self.ensure_url_prefix_not_null(self.INTERNATIONAL_STREET_API_URL)
        return InternationalStreetClient(self.build_sender(), self.serializer)

    def build_us_autocomplete_api_client(self):
        self.ensure_url_prefix_not_null(self.US_AUTOCOMPLETE_API_URL)
        return USAutocompleteClient(self.build_sender(), self.serializer)

    def build_us_extract_api_client(self):
        self.ensure_url_prefix_not_null(self.US_EXTRACT_API_URL)
        return USExtractClient(self.build_sender(), self.serializer)

    def build_us_street_api_client(self):
        self.ensure_url_prefix_not_null(self.US_STREET_API_URL)
        return USStreetClient(self.build_sender(), self.serializer)

    def build_us_zipcode_api_client(self):
        self.ensure_url_prefix_not_null(self.US_ZIP_CODE_API_URL)
        return USZIPClient(self.build_sender(), self.serializer)

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

    def ensure_url_prefix_not_null(self, url):
        if self.url_prefix is None:
            self.url_prefix = url
