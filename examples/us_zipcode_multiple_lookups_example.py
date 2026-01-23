import os

from smartystreets_python_sdk import SharedCredentials, BasicAuthCredentials, exceptions, Batch, ClientBuilder
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

    client = ClientBuilder(credentials).build_us_zipcode_api_client()
    batch = Batch()

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-zipcode-api#input-fields

    batch.add(ZIPCodeLookup())
    batch[0].input_id = "011889998819991197253"  # Optional ID from your system
    batch[0].zipcode = "12345"  # A Lookup may have a ZIP Code, city and state, or city, state, and ZIP Code

    # Uncomment the below line to add a custom parameter
    # batch[0].add_custom_parameter("parameter", "value")

    batch.add(ZIPCodeLookup())
    batch[1].city = "Phoenix"
    batch[1].state = "Arizona"

    batch.add(ZIPCodeLookup("cupertino", "CA", "95014"))  # You can also set these with arguments

    assert len(batch) == 3

    try:
        client.send_batch(batch)
    except exceptions.SmartyException as err:
        print(err)
        return

    for i, lookup in enumerate(batch):
        result = lookup.result
        print("Lookup {}:\n".format(i))

        if result.status is not None:
            print("Status: " + result.status)
            print("Reason: " + result.reason)
            continue

        cities = result.cities
        print("{} City and State match(es):".format(len(cities)))

        for city in cities:
            print("City: " + city.city)
            print("State: " + city.state)
            print("Mailable City: {}".format(city.mailable_city))
            print("")

        zipcodes = result.zipcodes
        print("{} ZIP Code match(es):".format(len(zipcodes)))

        for zipcode in zipcodes:
            print("ZIP Code: " + zipcode.zipcode)
            print("County: " + zipcode.county_name)
            print("Latitude: {}".format(zipcode.latitude))
            print("Longitude: {}".format(zipcode.longitude))
            print("")

        print("***********************************")


if __name__ == "__main__":
    run()
