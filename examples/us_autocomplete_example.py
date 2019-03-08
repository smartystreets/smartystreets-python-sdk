import os

from smartystreets_python_sdk import StaticCredentials, ClientBuilder
from smartystreets_python_sdk.us_autocomplete import Lookup


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_autocomplete_api_client()

    # For complete list of lookup fields, refer to:
    # https://smartystreets.com/docs/cloud/us-autocomplete-api#http-request-input-fields

    lookup = Lookup()
    lookup.prefix = "4770 Lincoln Ave 0"
    lookup.max_suggestions = 10
    lookup.city_filter = ("Geneva", "Florence", "Bethlehem", "Athens")
    lookup.state_filter = ("Alabama", "Florida", "Georgia")
    lookup.prefer = ("Geneva, AL", "Bethlehem, FL")
    lookup.geolocate_type = "null"
    lookup.prefer_ratio = .333333

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        print(suggestion.text)

    lookup.add_state_filter('IL')
    lookup.max_suggestions = 5

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        print(suggestion.text)


if __name__ == "__main__":
    run()
