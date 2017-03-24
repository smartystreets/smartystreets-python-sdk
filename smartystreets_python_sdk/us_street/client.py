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
        smartyrequest.payload = self.serializer.serialize(converted_lookups)

        response = self.sender.send(smartyrequest)

        if response.error:
            raise response.error

        candidates = self.serializer.deserialize(response.payload)
        if candidates is None:
            candidates = []
        assign_candidates_to_lookups(batch, candidates)


def assign_candidates_to_lookups(batch, candidates):
    for raw_candidate in candidates:
        candidate = Candidate(raw_candidate)
        batch[candidate.input_index].result.append(candidate)


def remap_keys(obj):
    converted_obj = []
    for lookup in obj:
        converted_lookup = {}

        add_field(converted_lookup, 'street', lookup.street)
        add_field(converted_lookup, 'street2', lookup.street2)
        add_field(converted_lookup, 'secondary', lookup.secondary)
        add_field(converted_lookup, 'city', lookup.city)
        add_field(converted_lookup, 'state', lookup.state)
        add_field(converted_lookup, 'zipcode', lookup.zipcode)
        add_field(converted_lookup, 'lastline', lookup.lastline)
        add_field(converted_lookup, 'addressee', lookup.addressee)
        add_field(converted_lookup, 'urbanization', lookup.urbanization)
        add_field(converted_lookup, 'match', lookup.match)
        add_field(converted_lookup, 'candidates', lookup.candidates)

        converted_obj.append(converted_lookup)

    return converted_obj


def add_field(converted_lookup, key, value):
    if value:
        converted_lookup[key] = value
