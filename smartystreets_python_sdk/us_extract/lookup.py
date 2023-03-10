from smartystreets_python_sdk.us_street.match_type import MatchType


class Lookup:
    def __init__(self, text=None, html=None, aggressive=None, addresses_have_line_breaks=None,
                 addresses_per_line=None, match=MatchType.STRICT):
        """
        In addition to holding all input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/us-extract-api#http-request-input-fields"
        """
        self.result = None
        self.text = text
        self.html = html
        self.aggressive = aggressive
        self.addresses_have_line_breaks = addresses_have_line_breaks
        self.addresses_per_line = addresses_per_line
        self.match = match

