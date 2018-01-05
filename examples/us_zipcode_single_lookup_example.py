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

    lookup = Lookup()
    lookup.city = "Mountain View"
    lookup.state = "California"

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
