import os

from smartystreets_python_sdk import SharedCredentials, ClientBuilder
from smartystreets_python_sdk.us_autocomplete_pro import Lookup as AutocompleteProLookup, geolocation_type


def run():
    # key = "Your SmartyStreets Key here"
    # hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    key = os.environ['SMARTY_AUTH_WEB']
    hostname = os.environ['SMARTY_WEBSITE_DOMAIN']

    credentials = SharedCredentials(key, hostname)

    client = ClientBuilder(credentials).build_us_autocomplete_pro_api_client()
    lookup = AutocompleteProLookup('4770 Lincoln Ave O')

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        print suggestion.street_line, suggestion.city, ",", suggestion.state

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-autocomplete-api#http-request-input-fields

    lookup.add_city_filter('Ogden')
    lookup.add_state_filter('IL')
    lookup.add_city_preference('Fallon')
    lookup.add_state_preference('IL')
    lookup.max_results = 5
    lookup.prefer_geo = geolocation_type.NONE
    lookup.prefer_ratio = 100

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        print suggestion.street_line, suggestion.city, ",", suggestion.state


if __name__ == "__main__":
    run()
