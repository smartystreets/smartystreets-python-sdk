import os

from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_zipcode import Lookup


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_zipcode_api_client()

    # Documentation for input fields can be found at:
    # https://smartystreet.com/docs/us-zipcode-api#input-fields

    lookup = Lookup()
    lookup.input_id = "dfc33cb6-829e-4fea-aa1b-b6d6580f0817"  # Optional ID from your system
    lookup.city = "Mountain View"
    lookup.state = "California"
    lookup.zipcode = "94043"

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result
    zipcodes = result.zipcodes
    cities = result.cities

    for city in cities:
        print("\nCity: " + city.city)
        print("State: " + city.state)
        print("Mailable City: {}".format(city.mailable_city))

    for zipcode in zipcodes:
        print("\nZIP Code: " + zipcode.zipcode)
        print("Latitude: {}".format(zipcode.latitude))
        print("Longitude: {}".format(zipcode.longitude))


if __name__ == "__main__":
    run()
