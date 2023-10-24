from smartystreets_python_sdk.us_street.match_type import MatchType
from smartystreets_python_sdk.us_street.output_format import OutputFormat


class Lookup:
    def __init__(self, street=None, street2=None, secondary=None, city=None, state=None, zipcode=None, lastline=None,
                 addressee=None, urbanization=None, match=MatchType.STRICT, candidates=1, input_id=None,
                 outputformat=OutputFormat.DEFAULT):
        """
        In addition to holding all input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/us-street-api#input-fields"
        """
        self.result = []
        self.input_id = input_id
        self.street = street
        self.street2 = street2
        self.secondary = secondary
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.lastline = lastline
        self.addressee = addressee
        self.urbanization = urbanization
        self.match = match
        self.candidates = candidates
        self.outputformat = outputformat
