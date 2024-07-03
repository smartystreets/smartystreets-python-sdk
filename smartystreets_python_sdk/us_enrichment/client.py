from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from .lookup import FinancialLookup, PrincipalLookup, GeoReferenceLookup, Lookup
from .response import Response


class Client:
    def __init__(self, sender, serializer):
        """
        It is recommended to instantiate this class using ClientBuilder.build_us_enrichment_api_client()
        """
        self.sender = sender
        self.serializer = serializer

    def send_property_financial_lookup(self, smartykey):
        l = FinancialLookup(smartykey)
        send_lookup(self, l)
        return l.result

    def send_property_principal_lookup(self, smartykey):
        l = PrincipalLookup(smartykey)
        send_lookup(self, l)
        return l.result
    
    def send_geo_reference_lookup(self, smartykey):
        l = GeoReferenceLookup(smartykey)
        send_lookup(self, l)
        return l.result
    
    def send_generic_lookup(self, smartykey, dataset, dataSubset):
        l = Lookup(smartykey, dataset, dataSubset)
        send_lookup(self, l)
        return l.result


def send_lookup(client: Client, lookup):
    """
    Sends a Lookup object to the US Enrichment API and stores the result in the Lookup's result field.
    """
    if lookup is None or lookup.smartykey is None or not isinstance(lookup.smartykey, str) or len(
            lookup.smartykey.strip()) == 0:
        raise SmartyException('Client.send() requires a Lookup with the "smartykey" field set as a string')

    request = build_request(lookup)

    response = client.sender.send(request)
    if response.error:
        raise response.error

    response = client.serializer.deserialize(response.payload)
    result = []
    for candidate in response:
        result.append(Response(candidate))
    lookup.result = result
    return result


def build_request(lookup):
    request = Request()
    if lookup.dataSubset == None:
        request.url_components = lookup.smartykey + "/" + lookup.dataset
        return request
    
    request.url_components = lookup.smartykey + "/" + lookup.dataset + "/" + lookup.dataSubset

    return request
