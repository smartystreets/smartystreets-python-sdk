from smartystreets_python_sdk import StaticCredentials, ClientBuilder
from smartystreets_python_sdk.us_extract import Lookup


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_extract_api_client()

    text = "Here is some text.\r\nMy address is 3785 Las Vegs Av." \
           "\r\nLos Vegas, Nevada." \
           "\r\nMeet me at 1 Rosedale Baltimore Maryland, not at 123 Phony Street, Boise Idaho."

    # For complete list of lookup fields, refer to:
    # https://smartystreets.com/docs/cloud/us-extract-api#http-request-input-fields

    lookup = Lookup()
    lookup.text = text
    lookup.aggressive = True
    lookup.addresses_have_line_breaks = False
    lookup.addresses_per_line = 1

    result = client.send(lookup)

    metadata = result.metadata
    print('Found {} addresses.'.format(metadata.address_count))
    print('{} of them were valid.'.format(metadata.verified_count))
    print()

    addresses = result.addresses

    print('Addresses: \r\n**********************\r\n')
    for address in addresses:
        print('"{}"\n'.format(address.text))
        print('Verified? {}'.format(address.verified))
        if len(address.candidates) > 0:

            print('\nMatches:')

            for candidate in address.candidates:
                print(candidate.delivery_line_1)
                print(candidate.last_line)
                print()

        else:
            print()

        print('**********************\n')


if __name__ == "__main__":
    run()
