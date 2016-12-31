from .address import Address
from .result import Result
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

        result = self.serializer.deserialize(response.payload)
        if result is None:
            result = {}
        assign_result_to_lookups(batch, result)


def assign_result_to_lookups(batch, raw_result):
    # valid_addresses = [x for x in result["addresses"] if x.get("verified", None) is True]
    result = Result(raw_result)
    for raw_address in result.addresses:
        address = Address(raw_address)
        batch[address.input_index].result.append(address)


def remap_keys(obj):
    converted_obj = []
    for lookup in obj:
        converted_lookup = {}

        converted_lookup['html'] = lookup.html
        converted_lookup['aggressive'] = lookup.aggressive
        converted_lookup['addr_line_breaks'] = lookup.addr_line_breaks
        converted_lookup['addr_per_line'] = lookup.addr_per_line
        converted_lookup[''] = lookup.input
        converted_obj.append(converted_lookup)

    return converted_obj
