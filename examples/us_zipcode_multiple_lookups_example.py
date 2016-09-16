import os

from smartystreets_python_sdk import StaticCredentials
from smartystreets_python_sdk.us_zipcode import ClientBuilder, Batch, Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build()
    batch = Batch()
    lookups = []

    lookup0 = Lookup()
    lookup0.zipcode = "12345"  # A Lookup may have a ZIP Code, city and state, or city, state, and ZIP Code
    lookups.append(lookup0)

    lookup1 = Lookup()
    lookup1.city = "Phoenix"
    lookup1.state = "Arizona"
    lookups.append(lookup1)

    lookup2 = Lookup("cupertino", "CA", "95014")  # You can also set these with arguments
    lookups.append(lookup2)

    for lookup in lookups:
        if batch.is_full():
            print "Batch is full"
            break

        batch.add(lookup)

    assert batch.size() == 3

    client.send_batch(batch)

    for i in range(0, batch.size()):
        result = lookups[i].result
        print "Lookup {}:\n".format(i)

        if result.status is not None:
            print "Status: " + result.status
            print "Reason: " + result.reason
            continue
        

        cities = result.cities
        print "{} City and State match(es):".format(len(cities))

        for city in cities:
            print "City: " + city.city
            print "State: " + city.state
            print "Mailable City: {}".format(city.mailable_city)
            print ""

        zipcodes = result.zipcodes
        print "{} ZIP Code match(es):".format(len(zipcodes))

        for zipcode in zipcodes:
            print "ZIP Code: " + zipcode.zipcode
            print "County: " + zipcode.county_name
            print "Latitude: {}".format(zipcode.latitude)
            print "Longitude: {}".format(zipcode.longitude)
            print ""

        print "***********************************"

if __name__ == "__main__":
    run()
