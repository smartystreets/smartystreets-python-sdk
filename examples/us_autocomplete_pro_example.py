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

    # The appropriate license values to be used for your subscriptions
    # can be found on the Subscriptions page of the account dashboard.
    # https://www.smartystreets.com/docs/cloud/licensing
    client = ClientBuilder(credentials).with_licenses(["us-autocomplete-pro-cloud"]).build_us_autocomplete_pro_api_client()
    lookup = AutocompleteProLookup('1042 W Center')

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        print suggestion.street_line, suggestion.city, ",", suggestion.state

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-autocomplete-api#http-request-input-fields

    lookup.add_state_filter('CO')
    lookup.add_state_filter('UT')
    lookup.add_city_filter('Denver')
    lookup.add_city_filter('Orem')
    lookup.add_state_preference('CO')
    lookup.add_state_preference('UT')
    lookup.add_city_preference('Denver')
    lookup.selected = '1042 W Center St Apt A (24) Orem UT 84057'
    lookup.max_results = 5
    lookup.prefer_geo = geolocation_type.NONE
    lookup.prefer_ratio = 33
    lookup.source = 'all'

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        print suggestion.street_line, suggestion.city, ",", suggestion.state


if __name__ == "__main__":
    run()
