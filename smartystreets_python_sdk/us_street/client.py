from smartystreets_python_sdk.us_street import Candidate
from smartystreets_python_sdk import Request, Batch


class Client:
    def __init__(self, sender, serializer):
        self.sender = sender
        self.serializer = serializer

    def send_lookup(self, lookup):
        batch = Batch()
        batch.add(lookup)
        self.send_batch(batch)

    def send_batch(self, batch):
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

        converted_lookup['street'] = lookup.street
        converted_lookup['street2'] = lookup.street2
        converted_lookup['secondary'] = lookup.secondary
        converted_lookup['city'] = lookup.city
        converted_lookup['state'] = lookup.state
        converted_lookup['zipcode'] = lookup.zipcode
        converted_lookup['lastline'] = lookup.lastline
        converted_lookup['addressee'] = lookup.addressee
        converted_lookup['urbanization'] = lookup.urbanization
        converted_lookup['match'] = lookup.match
        converted_lookup['candidates'] = lookup.candidates

        converted_obj.append(converted_lookup)

    return converted_obj
