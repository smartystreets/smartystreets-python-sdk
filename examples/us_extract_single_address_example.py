import os
from smartystreets_python_sdk import StaticCredentials, exceptions
from smartystreets_python_sdk.us_extract import ClientBuilder, Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build()

    lookup = Lookup()
    lookup.aggressive = False
    lookup.addr_line_breaks = False
    lookup.addr_per_line = 1
    lookup.input = """Bionic Emergency Services 14300 Northwest Freeway, # B-05 Houston, TX 77040 Ph:1-713-338-2424 Fax: 1-832-442-5804 Tax ID: 27-3522533  Insured: Property:  Beverly Young 2129 Tangley Houston, TX 77005  Claim Rep.: Davie Mankin Position: Property Loss Appraiser Estimator: Davie Mankin Position: Property Loss Appraiser Reference: Company: Chubb Insurance  Claim Number: 040545025941  Policy Number:  Type of Loss: Water Damage  Date of Loss: 4/18/2015 Date Inspected:  Price List: Estimate:  TXHO8X_APR15 Restoration/Service/Remodel BES-BYOUNG  Date Received: Date Entered: 4/24/2015 8:12 PM  THE FOLLOWING IS A CATEGORY 2 WATER LOSS DRY DOWN ESTIMATE FOR THE ABOVE ADDRESS. THIS ESTIMATE MAY INCLUDE WATER EXTRACTION, REMOVAL OF MATERIALS, DRYING RELATED EQUIPMENT. ALL WORK IS TO BE IS TO BE PREFORMED IN ACCORDANCE WITH THE IICRC'S S500/S520STANDARDS AND GUIDLINES. IN THE EVENT YOU HAVE ANY QUESTIONS, COMMENTS OR CONCERNS PLEASE CONTACT OUR OFFICES. THANK YOU FOR PLACING YOUR TRUST IN BIONIC EMERGENCY SERVICES. DAVIE MANKIN"""

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result

    if not result:
        print("No candidates. This means the address is not valid.")
        return

    for x in result:
        print(x.text)

if __name__ == "__main__":
    run()
