import os

from smartystreets_python_sdk import SharedCredentials, BasicAuthCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_zipcode import Lookup as ZIPCodeLookup


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

    # Documentation for input fields can be found at:
    # https://smartystreet.com/docs/us-zipcode-api#input-fields

    client = ClientBuilder(credentials).build_us_zipcode_api_client()

    lookup = ZIPCodeLookup()
    lookup.input_id = "dfc33cb6-829e-4fea-aa1b-b6d6580f0817"  # Optional ID from your system
    lookup.city = "Mountain View"
    lookup.state = "California"
    lookup.zipcode = "94043"

    # Uncomment the below line to add a custom parameter
    # lookup.add_custom_parameter("parameter", "value")

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
        print("County: {}".format(zipcode.county_name))


if __name__ == "__main__":
    run()
