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

        smartyrequest.payload = self.serializer.serialize(batch.all_lookups)

        response = self.sender.send(smartyrequest)

        candidates = self.serializer.deserialize(response.payload)
        if candidates is None:
            candidates = []
        assign_candidates_to_lookups(batch, candidates)


def assign_candidates_to_lookups(batch, candidates):
    for candidate in candidates:
        batch[candidate.inputindex].result.append(candidate)
