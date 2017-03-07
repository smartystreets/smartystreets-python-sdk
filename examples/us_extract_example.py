import os
from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_extract import Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_extract_api_client()

    text = "Here is some text.\r\nMy address is 3785 Las Vegs Av." \
           "\r\nLos Vegas, Nevada." \
           "\r\nMeet me at 1 Rosedale Baltimore Maryland, not at 123 Phony Street, Boise Idaho."

    lookup = Lookup(text)

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
        if len(address.api_output) > 0:

            print('\nMatches:')

            for candidate in address.api_output:
                print(candidate.delivery_line_1)
                print(candidate.last_line)
                print()

        else:
            print()

        print('**********************\n')


if __name__ == "__main__":
    run()
