import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, BasicAuthCredentials, ClientBuilder
from smartystreets_python_sdk.us_autocomplete_pro import Lookup as AutocompleteProLookup, geolocation_type


def run():
    # key = "Your SmartyStreets Key here"
    # hostname = "Your Hostname here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # for client-side requests (browser/mobile), use this code:
    # key = os.environ['SMARTY_AUTH_WEB']
    # hostname = os.environ['SMARTY_WEBSITE_DOMAIN']
    #
    # credentials = SharedCredentials(key, hostname)

    # for server-to-server requests, use this code:
    auth_id = os.environ['SMARTY_AUTH_ID']
    auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = BasicAuthCredentials(auth_id, auth_token)

    # for server-to-server requests, use this code:
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']
    #
    # credentials = BasicAuthCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_autocomplete_pro_api_client()
    
    lookup = AutocompleteProLookup('1042 W Center')

    # Uncomment the below line to add a custom parameter
    # lookup.add_custom_parameter("parameter", "value")

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        print(suggestion.street_line + " " + suggestion.city, suggestion.state, sep=", ")

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-autocomplete-api#http-request-input-fields

    lookup.add_city_filter('Denver,Aurora,CO')
    lookup.add_city_filter('Orem,UT')
    lookup.add_state_preference('CO')
    # lookup.selected = '1042 W Center St Apt A (24) Orem UT 84057'
    lookup.max_results = 5
    lookup.prefer_geo = geolocation_type.NONE
    lookup.prefer_ratio = 33
    lookup.source = 'all'

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        print(suggestion.street_line + " " + suggestion.city + ", " + suggestion.state)


if __name__ == "__main__":
    run()
