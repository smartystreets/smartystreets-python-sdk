import os

from smartystreets_python_sdk import StaticCredentials, exceptions
from smartystreets_python_sdk.us_zipcode import ClientBuilder, Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build()

    lookup = Lookup()
    lookup.city = "Mountain View"
    lookup.state = "California"

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as e:
        print(e.message)
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
