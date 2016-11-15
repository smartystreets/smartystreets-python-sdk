from smartystreets_python_sdk.us_zipcode import Result
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

        results = self.serializer.deserialize(response.payload)
        if results is None:
            results = []
        assign_results_to_lookups(batch, results)


def assign_results_to_lookups(batch, results):
    for raw_result in results:
        result = Result(raw_result)
        batch[result.input_index].result = result


def remap_keys(obj):
    converted_obj = []
    for lookup in obj:
        converted_lookup = {}

        converted_lookup['city'] = lookup.city
        converted_lookup['state'] = lookup.state
        converted_lookup['zipcode'] = lookup.zipcode

        converted_obj.append(converted_lookup)

    return converted_obj
