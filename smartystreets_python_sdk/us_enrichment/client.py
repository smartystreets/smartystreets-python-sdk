from smartystreets_python_sdk import Request
from smartystreets_python_sdk.exceptions import SmartyException
from .lookup import FinancialLookup, PrincipalLookup
from .response import FinancialResponse, PrincipalResponse

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

def send_lookup(client : Client, lookup):
    """
    Sends a Lookup object to the US Enrichment API and stores the result in the Lookup's result field.
    """
    if lookup is None or lookup.smartykey is None or not isinstance(lookup.smartykey, str) or len(lookup.smartykey.strip()) == 0:
        raise SmartyException('Client.send() requires a Lookup with the "smartykey" field set')
    
    request = build_request(lookup)

    response = client.sender.send(request)
    if response.error:
        raise response.error
    
    result = get_result(client.serializer.deserialize(response.payload))
    lookup.result = result
    return result

def build_request(lookup):
    request = Request()
    request.content_type = 'text_plain'
    add_parameter(request, "smartykey", lookup.smartykey)
    add_parameter(request, "dataset", lookup.dataset)
    add_parameter(request, "datasubset", lookup.dataSubset) #TODO This isn't right, figure out how to change the url we are using.

    return request

def add_parameter(request, key, value):
    if value and value != 'none':
        request.parameters[key] = value

def get_result(obj, lookup):
    if type(lookup) == FinancialLookup:
        return FinancialResponse(obj)
    if type(lookup) == PrincipalLookup:
        return PrincipalResponse(obj)
