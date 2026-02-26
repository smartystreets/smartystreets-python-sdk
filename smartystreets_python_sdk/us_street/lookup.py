from smartystreets_python_sdk.us_street.match_type import MatchType
from smartystreets_python_sdk.us_street.output_format import OutputFormat
import json


class Lookup:
    def __init__(self, street=None, street2=None, secondary=None, city=None, state=None, zipcode=None, lastline=None,
                 addressee=None, urbanization=None, match=None, candidates=0, input_id=None,
                 outputformat=OutputFormat.DEFAULT, county_source=None):
        """
        In addition to holding all input data for this lookup, this class also will contain the result
        of the lookup after it comes back from the API.
        
        See "https://smartystreets.com/docs/cloud/us-street-api#input-fields"
        """
        self.result = []
        self.custom_parameter_array = {}
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
        self.county_source = county_source

    def add_custom_parameter(self, parameter, value):
        self.custom_parameter_array[parameter] = value

    def to_dict(self):
        result =  {
            "input_id": self.input_id,
            "street": self.street,
            "street2": self.street2,
            "secondary": self.secondary,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "lastline": self.lastline,
            "addressee": self.addressee,
            "urbanization": self.urbanization,
            "match": self.match,
            "candidates": self.candidates,
            "outputformat": self.outputformat,
            "county_source": self.county_source,
            "result": [candidate.to_dict() for candidate in self.result],
            "custom_parameter_array": self.custom_parameter_array
        }
        return {k: v for k, v in result.items() if v is not None}

    def to_json(self):
        return json.dumps(self.to_dict())