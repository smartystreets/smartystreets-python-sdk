from smartystreets_python_sdk.us_zipcode import Batch, Result
from smartystreets_python_sdk import Request


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

        smartyrequest.payload = self.serializer.serialize(batch.all_lookups)

        response = self.sender.send(smartyrequest)

        results = self.serializer.deserialize(response.payload)
        if results is None:
            results = []
        assign_results_to_lookups(batch, results)


def assign_results_to_lookups(batch, results):
    for raw_result in results:
        result = Result(raw_result)
        batch[result.input_index].result = result
