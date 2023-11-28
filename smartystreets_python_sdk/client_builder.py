import smartystreets_python_sdk as smarty
from smartystreets_python_sdk.us_street import Client as USStreetClient
from smartystreets_python_sdk.us_zipcode import Client as USZIPClient
from smartystreets_python_sdk.us_extract import Client as USExtractClient
from smartystreets_python_sdk.us_autocomplete import Client as USAutocompleteClient
from smartystreets_python_sdk.us_autocomplete_pro import Client as USAutocompleteProClient
from smartystreets_python_sdk.us_reverse_geo import Client as USReverseGeoClient
from smartystreets_python_sdk.international_street import Client as InternationalStreetClient
from smartystreets_python_sdk.international_autocomplete import Client as InternationalAutocompleteClient
from smartystreets_python_sdk.us_enrichment import Client as USEnrichmentClient


class ClientBuilder:
    def __init__(self, signer):
        """
        The ClientBuilder class helps you build a client object for one of the supported SmartyStreets APIs.
        You can use ClientBuilder's methods to customize settings like maximum retries or timeout duration.
        These methods are chainable, so you can usually get set up with one line of code.
        """
        self.signer = signer
        self.serializer = smarty.NativeSerializer()
        self.http_sender = None
        self.max_retries = 5
        self.max_timeout = 10
        self.url_prefix = None
        self.proxy = None
        self.debug = None
        self.header = None
        self.licenses = []
        self.INTERNATIONAL_STREET_API_URL = "https://international-street.api.smarty.com/verify"
        self.INTERNATIONAL_AUTOCOMPLETE_API_URL = "https://international-autocomplete.api.smarty.com/v2/lookup"
        self.US_AUTOCOMPLETE_API_URL = "https://us-autocomplete.api.smarty.com/suggest"
        self.US_AUTOCOMPLETE_PRO_API_URL = "https://us-autocomplete-pro.api.smarty.com/lookup"
        self.US_EXTRACT_API_URL = "https://us-extract.api.smarty.com"
        self.US_STREET_API_URL = "https://us-street.api.smarty.com/street-address"
        self.US_ZIP_CODE_API_URL = "https://us-zipcode.api.smarty.com/lookup"
        self.US_REVERSE_GEO_API_URL = "https://us-reverse-geo.api.smarty.com/lookup"
        self.US_ENRICHMENT_API_URL = "https://us-enrichment.api.smarty.com/lookup/"

    def retry_at_most(self, max_retries):
        """
        Sets the maximum number of times to retry sending the request to the API. (Default is 5)

        Returns self to accommodate method chaining.
        """
        self.max_retries = max_retries
        return self

    def with_max_timeout(self, max_timeout):
        """
        The maximum time (in seconds) to wait for a connection, and also to wait for
        the response to be read. (Default is 10)

        Returns self to accommodate method chaining.
        """
        self.max_timeout = max_timeout
        return self

    def with_sender(self, sender):
        """
        Default is a series of nested senders. (See build_sender()

        Returns self to accommodate method chaining.
        """
        self.http_sender = sender
        return self

    def with_serializer(self, serializer):
        """
        Changes the Serializer from the default.

        Returns self to accommodate method chaining.
        """
        self.serializer = serializer
        return self

    def with_base_url(self, base_url):
        """
        This may be useful when using a local installation of the SmartyStreets APIs.
        base_url is a string that defaults to the URL for the API corresponding to the Client object being built.

        Returns self to accommodate method chaining.
        """
        self.url_prefix = base_url
        return self

    def with_proxy(self, host, username=None, password=None):
        """
        Assigns a proxy through which to send all Lookups.
        :param host: The proxy host including port, but not scheme. (example: localhost:8080)
        :param username: Username to authenticate with the proxy server
        :param password: Password to authenticate with the proxy server
        :return: Returns self to accommodate method chaining.
        """
        self.proxy = smarty.Proxy(host, username, password)
        return self

    def with_custom_header(self, custom_header):
        """
        Create custom headers when necessary.
        :param custom_header: Input your custom headers
        :return: Returns self to accommodate method chaining
        """
        self.header = custom_header
        return self

    def with_debug(self):
        """
        Enables debug mode, which will print information about the HTTP request and response to the console.

        Returns self to accommodate method chaining.
        """
        self.debug = True
        return self

    def with_licenses(self, licenses):
        """
        Allows the caller to specify the subscription license (aka "track") they wish to use.
        :param licenses: Input licenses
        :return: Returns self to accommodate method chaining
        """
        self.licenses = licenses
        return self

    def build_international_street_api_client(self):
        self.ensure_url_prefix_not_null(self.INTERNATIONAL_STREET_API_URL)
        return InternationalStreetClient(self.build_sender(), self.serializer)

    def build_international_autocomplete_api_client(self):
        self.ensure_url_prefix_not_null(self.INTERNATIONAL_AUTOCOMPLETE_API_URL)
        return InternationalAutocompleteClient(self.build_sender(), self.serializer)

    def build_us_autocomplete_api_client(self):
        self.ensure_url_prefix_not_null(self.US_AUTOCOMPLETE_API_URL)
        return USAutocompleteClient(self.build_sender(), self.serializer)

    def build_us_autocomplete_pro_api_client(self):
        self.ensure_url_prefix_not_null(self.US_AUTOCOMPLETE_PRO_API_URL)
        return USAutocompleteProClient(self.build_sender(), self.serializer)

    def build_us_extract_api_client(self):
        self.ensure_url_prefix_not_null(self.US_EXTRACT_API_URL)
        return USExtractClient(self.build_sender(), self.serializer)

    def build_us_street_api_client(self):
        self.ensure_url_prefix_not_null(self.US_STREET_API_URL)
        return USStreetClient(self.build_sender(), self.serializer)

    def build_us_zipcode_api_client(self):
        self.ensure_url_prefix_not_null(self.US_ZIP_CODE_API_URL)
        return USZIPClient(self.build_sender(), self.serializer)

    def build_us_reverse_geo_api_client(self):
        self.ensure_url_prefix_not_null(self.US_REVERSE_GEO_API_URL)
        return USReverseGeoClient(self.build_sender(), self.serializer)

    def build_us_enrichment_api_client(self):
        self.ensure_url_prefix_not_null(self.US_ENRICHMENT_API_URL)
        return USEnrichmentClient(self.build_sender(), self.serializer)

    def build_sender(self):
        if self.http_sender is not None:
            return self.http_sender

        sender = smarty.RequestsSender(self.max_timeout, self.proxy)
        sender.debug = self.debug

        sender = smarty.StatusCodeSender(sender)

        if self.header is not None:
            sender = smarty.CustomHeaderSender(self.header, sender)

        if self.signer is not None:
            sender = smarty.SigningSender(self.signer, sender)

        if self.max_retries > 0:
            sender = smarty.RetrySender(self.max_retries, sender)

        sender = smarty.URLPrefixSender(self.url_prefix, sender)

        sender = smarty.LicenseSender(self.licenses, sender)

        return sender

    def ensure_url_prefix_not_null(self, url):
        if self.url_prefix is None:
            self.url_prefix = url
