from smartystreets_python_sdk import StaticCredentials, exceptions, Batch, ClientBuilder
from smartystreets_python_sdk.us_zipcode import Lookup


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_zipcode_api_client()
    batch = Batch()

    # For complete list of input fields, refer to:
    # https://smartystreets.com/docs/us-street-api#input-fields

    batch.add(Lookup())
    batch[0].input_id = "011889998819991197253"
    batch[0].zipcode = "12345"  # A Lookup may have a ZIP Code, city and state, or city, state, and ZIP Code

    batch.add(Lookup())
    batch[1].city = "Phoenix"
    batch[1].state = "Arizona"

    batch.add(Lookup("cupertino", "CA", "95014"))  # You can also set these with arguments

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
