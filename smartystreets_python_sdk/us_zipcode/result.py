from typing import Any

from smartystreets_python_sdk.us_zipcode import City, ZipCode


class Result:
    """
    See "https://smartystreets.com/docs/cloud/us-zipcode-api#root"
    """
    def __init__(self, obj: dict) -> None:
        self.status: str | None = obj.get('status')
        self.reason: str | None = obj.get('reason')
        self.input_index: int | None = obj.get('input_index')
        self.cities: list[City] = obj.get('city_states', [])
        self.zipcodes: list[ZipCode] = obj.get('zipcodes', [])

        self.cities = convert_cities(self.cities)
        self.zipcodes = convert_zipcodes(self.zipcodes)

    def is_valid(self) -> bool:
        return self.status is None and self.reason is None


def convert_cities(cities: list[dict[str, Any]]) -> list[City]:
    converted_cities = []

    for city in cities:
        converted_cities.append(City(city))

    return converted_cities


def convert_zipcodes(zipcodes: list[dict[str, Any]]) -> list[ZipCode]:
    converted_zipcodes = []

    for zipcode in zipcodes:
        converted_zipcodes.append(ZipCode(zipcode))

    return converted_zipcodes

