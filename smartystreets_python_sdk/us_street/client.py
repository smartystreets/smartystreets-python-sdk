from smartystreets_python_sdk.us_street.match_type import MatchType
from smartystreets_python_sdk.us_street.output_format import OutputFormat

from smartystreets_python_sdk.us_street import Candidate
from smartystreets_python_sdk import Request, Batch


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_street_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send_lookup(self, lookup):
        """
        Sends a Lookup object to the US Street API and stores the result in the Lookup's result field.
        """
        batch = Batch()
        batch.add(lookup)
        self.send_batch(batch)

    def send_batch(self, batch):
        """
        Sends a Batch object containing no more than 100 Lookup objects to the US Street API and stores the
        results in the result field of the Lookup object.
        """
        smartyrequest = Request()

        if len(batch) == 0:
            return

        converted_lookups = remap_keys(batch.all_lookups)

        if len(batch) == 1:
            smartyrequest.parameters = converted_lookups[0]
        else:
            smartyrequest.payload = self.serializer.serialize(converted_lookups)

        response = self.sender.send(smartyrequest)

        if response.error:
            raise response.error

        candidates = self.serializer.deserialize(response.payload) or []
        assign_candidates_to_lookups(batch, candidates)


def assign_candidates_to_lookups(batch, candidates):
    for raw_candidate in candidates:
        candidate = Candidate(raw_candidate)
        batch[candidate.input_index].result.append(candidate)


def remap_keys(obj):
    converted_obj = []
    for lookup in obj:
        converted_lookup = {}

        if (lookup.match == MatchType.ENHANCED or lookup.match == "enhanced") and lookup.candidates == 1:
            add_field(converted_lookup, 'candidates', 5)
        else:
            add_field(converted_lookup, 'candidates', lookup.candidates)

        add_field(converted_lookup, 'input_id', lookup.input_id)
        add_field(converted_lookup, 'street', lookup.street)
        add_field(converted_lookup, 'street2', lookup.street2)
        add_field(converted_lookup, 'secondary', lookup.secondary)
        add_field(converted_lookup, 'city', lookup.city)
        add_field(converted_lookup, 'state', lookup.state)
        add_field(converted_lookup, 'zipcode', lookup.zipcode)
        add_field(converted_lookup, 'lastline', lookup.lastline)
        add_field(converted_lookup, 'addressee', lookup.addressee)
        add_field(converted_lookup, 'urbanization', lookup.urbanization)
        if isinstance(lookup.match, MatchType):
            add_field(converted_lookup, 'match', lookup.match.value)
        else:
            add_field(converted_lookup, 'match', lookup.match)

        if isinstance(lookup.outputformat, OutputFormat):
            add_field(converted_lookup, 'format', lookup.outputformat.value)
        else:
            add_field(converted_lookup, 'format', lookup.outputformat)

        converted_obj.append(converted_lookup)

    return converted_obj


def add_field(converted_lookup, key, value):
    if value:
        converted_lookup[key] = value
