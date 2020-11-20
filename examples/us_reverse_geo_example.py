import os

from smartystreets_python_sdk import StaticCredentials, ClientBuilder
from smartystreets_python_sdk.us_reverse_geo import Lookup


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_us_reverse_geo_api_client()

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/cloud/us-reverse-geo-api#http-input-fields

    lookup = Lookup(40.111111, -111.111111)

    results = client.send(lookup)
    result = results[0]

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


if __name__ == "__main__":
    run()
