import unittest

from smartystreets_python_sdk import NativeSerializer
from smartystreets_python_sdk.international_street import Candidate


class TestCandidate(unittest.TestCase):
    def test_all_fields_filled_correctly(self):
        response_payload = "[{\"organization\":\"1\",\"address1\":\"2\",\"address2\":\"3\","\
                "\"address3\":\"4\",\"address4\":\"5\",\"address5\":\"6\",\"address6\":\"7\",\"address7\":\"8\","\
                "\"address8\":\"9\",\"address9\":\"10\",\"address10\":\"11\",\"address11\":\"12\",\"address12\":\"13\","\
                "\"components\":{\"country_iso_3\":\"14\",\"super_administrative_area\":\"15\","\
                "\"administrative_area\":\"16\",\"sub_administrative_area\":\"17\",\"dependent_locality\":\"18\","\
                "\"dependent_locality_name\":\"19\",\"double_dependent_locality\":\"20\",\"locality\":\"21\","\
                "\"postal_code\":\"22\",\"postal_code_short\":\"23\",\"postal_code_extra\":\"24\","\
                "\"premise\":\"25\",\"premise_extra\":\"26\",\"premise_number\":\"27\",\"premise_type\":\"28\","\
                "\"thoroughfare\":\"29\",\"thoroughfare_predirection\":\"30\",\"thoroughfare_postdirection\":\"31\","\
                "\"thoroughfare_name\":\"32\",\"thoroughfare_trailing_type\":\"33\",\"thoroughfare_type\":\"34\","\
                "\"dependent_thoroughfare\":\"35\",\"dependent_thoroughfare_predirection\":\"36\","\
                "\"dependent_thoroughfare_postdirection\":\"37\",\"dependent_thoroughfare_name\":\"38\","\
                "\"dependent_thoroughfare_trailing_type\":\"39\",\"dependent_thoroughfare_type\":\"40\","\
                "\"building\":\"41\",\"building_leading_type\":\"42\",\"building_name\":\"43\","\
                "\"building_trailing_type\":\"44\",\"sub_building_type\":\"45\",\"sub_building_number\":\"46\","\
                "\"sub_building_name\":\"47\",\"sub_building\":\"48\",\"post_box\":\"49\",\"post_box_type\":\"50\","\
                "\"post_box_number\":\"51\"},\"metadata\":{\"latitude\":52.0,\"longitude\":53.0,"\
                "\"geocode_precision\":\"54\",\"max_geocode_precision\":\"55\",\"address_format\":\"56\"},"\
                "\"analysis\":{\"verification_status\":\"57\",\"address_precision\":\"58\",\"max_address_precision\":\"59\"}}]"

        serializer = NativeSerializer()
        candidate = Candidate(serializer.deserialize(response_payload)[0])

        self.assertEqual("1", candidate.organization)
        self.assertEqual("2", candidate.address1)
        self.assertEqual("3", candidate.address2)
        self.assertEqual("4", candidate.address3)
        self.assertEqual("5", candidate.address4)
        self.assertEqual("6", candidate.address5)
        self.assertEqual("7", candidate.address6)
        self.assertEqual("8", candidate.address7)
        self.assertEqual("9", candidate.address8)
        self.assertEqual("10", candidate.address9)
        self.assertEqual("11", candidate.address10)
        self.assertEqual("12", candidate.address11)
        self.assertEqual("13", candidate.address12)

        components = candidate.components
        self.assertIsNotNone(components)
        self.assertEqual("14", components.country_iso_3)
        self.assertEqual("15", components.super_administrative_area)
        self.assertEqual("16", components.administrative_area)
        self.assertEqual("17", components.sub_administrative_area)
        self.assertEqual("18", components.dependent_locality)
        self.assertEqual("19", components.dependent_locality_name)
        self.assertEqual("20", components.double_dependent_locality)
        self.assertEqual("21", components.locality)
        self.assertEqual("22", components.postal_code)
        self.assertEqual("23", components.postal_code_short)
        self.assertEqual("24", components.postal_code_extra)
        self.assertEqual("25", components.premise)
        self.assertEqual("26", components.premise_extra)
        self.assertEqual("27", components.premise_number)
        self.assertEqual("28", components.premise_type)
        self.assertEqual("29", components.thoroughfare)
        self.assertEqual("30", components.thoroughfare_predirection)
        self.assertEqual("31", components.thoroughfare_postdirection)
        self.assertEqual("32", components.thoroughfare_name)
        self.assertEqual("33", components.thoroughfare_trailing_type)
        self.assertEqual("34", components.thoroughfare_type)
        self.assertEqual("35", components.dependent_thoroughfare)
        self.assertEqual("36", components.dependent_thoroughfare_predirection)
        self.assertEqual("37", components.dependent_thoroughfare_postdirection)
        self.assertEqual("38", components.dependent_thoroughfare_name)
        self.assertEqual("39", components.dependent_thoroughfare_trailing_type)
        self.assertEqual("40", components.dependent_thoroughfare_type)
        self.assertEqual("41", components.building)
        self.assertEqual("42", components.building_leading_type)
        self.assertEqual("43", components.building_name)
        self.assertEqual("44", components.building_trailing_type)
        self.assertEqual("45", components.sub_building_type)
        self.assertEqual("46", components.sub_building_number)
        self.assertEqual("47", components.sub_building_name)
        self.assertEqual("48", components.sub_building)
        self.assertEqual("49", components.post_box)
        self.assertEqual("50", components.post_box_type)
        self.assertEqual("51", components.post_box_number)

        metadata = candidate.metadata
        self.assertIsNotNone(metadata)
        self.assertEqual(52, metadata.latitude, 0.001)
        self.assertEqual(53, metadata.longitude, 0.001)
        self.assertEqual("54", metadata.geocode_precision)
        self.assertEqual("55", metadata.max_geocode_precision)
        self.assertEqual("56", metadata.address_format)

        analysis = candidate.analysis
        self.assertIsNotNone(analysis)
        self.assertEqual("57", analysis.verification_status)
        self.assertEqual("58", analysis.address_precision)
        self.assertEqual("59", analysis.max_address_precision)
