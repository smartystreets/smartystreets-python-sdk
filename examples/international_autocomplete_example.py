import os

from smartystreets_python_sdk import SharedCredentials, ClientBuilder
from smartystreets_python_sdk.international_autocomplete import Lookup as InternationalAutocompleteLookup


def run():
    key = "Your SmartyStreets Key here"
    hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # key = os.environ['SMARTY_AUTH_WEB']
    # hostname = os.environ['SMARTY_WEBSITE_DOMAIN']

    credentials = SharedCredentials(key, hostname)

    # The appropriate license values to be used for your subscriptions
    # can be found on the Subscriptions page of the account dashboard.
    # https://www.smartystreets.com/docs/cloud/licensing
    client = ClientBuilder(credentials).with_licenses(["international-autocomplete-cloud"])\
        .build_international_autocomplete_api_client()
    lookup = InternationalAutocompleteLookup('Louis')
    lookup.country = "FRA"

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        print suggestion.street, suggestion.locality, ",", suggestion.administrative_area

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-autocomplete-api#http-request-input-fields

    lookup.locality = "Paris"

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        print suggestion.street, suggestion.locality, ",", suggestion.administrative_area


if __name__ == "__main__":
    run()
