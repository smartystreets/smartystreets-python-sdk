from smartystreets_python_sdk.us_extract import Address
from smartystreets_python_sdk.us_extract import Metadata


class Result:
    def __init__(self, obj=None):
        """
        See "https://smartystreets.com/docs/cloud/us-extract-api#http-response-status"
        """
        self.metadata = Metadata(obj.get('meta', {}))
        self.addresses = obj.get('addresses', [])

        self.addresses = convert_addresses(self.addresses)


def convert_addresses(addresses):
    converted_addresses = []

    for address in addresses:
        converted_addresses.append(Address(address))

    return converted_addresses
