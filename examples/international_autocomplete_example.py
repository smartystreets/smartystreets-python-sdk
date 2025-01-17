import os

from smartystreets_python_sdk import SharedCredentials, ClientBuilder, StaticCredentials
from smartystreets_python_sdk.international_autocomplete import Lookup as InternationalAutocompleteLookup


def run():
    # key = "Your SmartyStreets Key here"
    # hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # for client-side requests (browser/mobile), use this code:
    key = os.environ['SMARTY_AUTH_WEB']
    hostname = os.environ['SMARTY_WEBSITE_DOMAIN']

    credentials = SharedCredentials(key, hostname)

    # for server-to-server requests, use this code:
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']
    #
    # credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_international_autocomplete_api_client()

    # (Advanced) Uncomment the below line to explicitly specify a license value
    # client = ClientBuilder(credentials).with_licenses(["international-autocomplete-v2-cloud"]).build_international_autocomplete_api_client()

    # The appropriate license values to be used for your subscriptions
    # can be found on the Subscriptions page of the account dashboard.
    # https://www.smartystreets.com/docs/cloud/licensing
    
    lookup = InternationalAutocompleteLookup('Louis')
    lookup.country = "FRA"

    # Uncomment the below line to add a custom parameter
    # lookup.add_custom_parameter("parameter", "value")

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        if suggestion.address_text:
            print(str(suggestion.entries) + " " + suggestion.address_text + " " + suggestion.address_id)
        else:
            print(suggestion.street + " " + suggestion.locality, suggestion.administrative_area, sep=", ")

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-autocomplete-api#http-request-input-fields

    lookup.locality = "Paris"

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        if suggestion.address_text:
            print(str(suggestion.entries) + " " + suggestion.address_text + " " + suggestion.address_id)
        else:
            print(suggestion.street + " " + suggestion.locality, suggestion.administrative_area, sep=", ")


if __name__ == "__main__":
    run()
