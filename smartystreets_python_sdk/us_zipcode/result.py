from smartystreets_python_sdk.us_zipcode import City, ZipCode


class Result:
    """
    See "https://smartystreets.com/docs/cloud/us-zipcode-api#root"
    """
    def __init__(self, obj):
        self.status = obj.get('status')
        self.reason = obj.get('reason')
        self.input_index = obj.get('input_index')
        self.cities = obj.get('city_states', [])
        self.zipcodes = obj.get('zipcodes', [])

        self.cities = convert_cities(self.cities)
        self.zipcodes = convert_zipcodes(self.zipcodes)

    def is_valid(self):
        return self.status is None and self.reason is None


def convert_cities(cities):
    converted_cities = []

    for city in cities:
        converted_cities.append(City(city))

    return converted_cities


def convert_zipcodes(zipcodes):
    converted_zipcodes = []

    for zipcode in zipcodes:
        converted_zipcodes.append(ZipCode(zipcode))

    return converted_zipcodes

