from smartystreets_python_sdk.us_street import Batch
from smartystreets_python_sdk import Request


class Client:
    def __init__(self, urlprefix, sender, serializer):
        self.urlprefix = urlprefix
        self.sender = sender
        self.serializer = serializer

    def send_lookup(self, lookup):
        batch = Batch()
        batch.add(lookup)
        self.send_batch(batch)

    def send_batch(self, batch):
        smartyrequest = Request(self.urlprefix)

        if batch.size() == 0:
            return

        if batch.size() == 1:
            set_parameters(batch[0], smartyrequest)
        else:
            smartyrequest.payload = self.serializer.serialize(batch.all_lookups)

        response = self.sender.send(smartyrequest)

        candidates = self.serializer.deserialize(response.payload)
        if candidates is None:
            candidates = []
        assign_candidates_to_lookups(batch, candidates)


def set_parameters(address, request):
    request.parameters['street'] = address.street
    request.parameters['street2'] = address.street2
    request.parameters['secondary'] = address.secondary
    request.parameters['city'] = address.city
    request.parameters['state'] = address.state
    request.parameters['zipcode'] = address.zipcode
    request.parameters['lastline'] = address.lastline
    request.parameters['addressee'] = address.addressee
    request.parameters['urbanization'] = address.urbanization
    request.parameters['match'] = address.match

    if address.candidates != 1:
        request.parameters['candidates'] = address.candidates


def assign_candidates_to_lookups(batch, candidates):
    for candidate in candidates:
        batch[candidate.inputindex].result.append(candidate)
