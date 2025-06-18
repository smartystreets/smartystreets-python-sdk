import os

from smartystreets_python_sdk import SharedCredentials, StaticCredentials, ClientBuilder
from smartystreets_python_sdk.us_reverse_geo import Lookup


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

    client = ClientBuilder(credentials).build_us_reverse_geo_api_client()
    
    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/cloud/us-reverse-geo-api#http-input-fields

    lookup = Lookup(40.111111, -111.111111)

    # Uncomment the below line to add a custom parameter
    # lookup.add_custom_parameter("parameter", "value")

    results = client.send(lookup)

    for result in results:
        coordinate = result.coordinate
        print("Latitude: {}".format(coordinate.latitude))
        print("Longitude: {}".format(coordinate.longitude))

        print("Distance: {}".format(result.distance))

        address = result.address
        print("Street: {}".format(address.street))
        print("City: {}".format(address.city))
        print("State Abbreviation: {}".format(address.state_abbreviation))
        print("ZIP Code: {}".format(address.zipcode))
        print("License: {}".format(coordinate.get_license()))
        print()


if __name__ == "__main__":
    run()
