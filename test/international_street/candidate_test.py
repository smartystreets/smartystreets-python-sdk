import unittest

from smartystreets_python_sdk import NativeSerializer
from smartystreets_python_sdk.international_street import Candidate


class TestCandidate(unittest.TestCase):
    def test_all_fields_filled_correctly(self):
        response_payload = "[{\"input_id\":\"12345678\",\"organization\":\"1\",\"address1\":\"2\",\"address2\":\"3\","\
                "\"address3\":\"4\",\"address4\":\"5\",\"address5\":\"6\",\"address6\":\"7\",\"address7\":\"8\","\
                "\"address8\":\"9\",\"address9\":\"10\",\"address10\":\"11\",\"address11\":\"12\",\"address12\":\"13\","\
                "\"components\":{\"country_iso_3\":\"14\",\"super_administrative_area\":\"15\","\
                "\"administrative_area\":\"16\",\"administrative_area_iso2\":\"16.1\",\"administrative_area_short\":\"16.2\",\"administrative_area_long\":\"16.3\","\
                "\"sub_administrative_area\":\"17\",\"dependent_locality\":\"18\","\
                "\"dependent_locality_name\":\"19\",\"double_dependent_locality\":\"20\",\"locality\":\"21\","\
                "\"postal_code\":\"22\",\"postal_code_short\":\"23\",\"postal_code_extra\":\"24\","\
                "\"premise\":\"25\",\"premise_extra\":\"26\",\"premise_number\":\"27\"," \
                "\"premise_prefix_number\":\"27.5\",\"premise_type\":\"28\","\
                "\"thoroughfare\":\"29\",\"thoroughfare_predirection\":\"30\",\"thoroughfare_postdirection\":\"31\","\
                "\"thoroughfare_name\":\"32\",\"thoroughfare_trailing_type\":\"33\",\"thoroughfare_type\":\"34\","\
                "\"dependent_thoroughfare\":\"35\",\"dependent_thoroughfare_predirection\":\"36\","\
                "\"dependent_thoroughfare_postdirection\":\"37\",\"dependent_thoroughfare_name\":\"38\","\
                "\"dependent_thoroughfare_trailing_type\":\"39\",\"dependent_thoroughfare_type\":\"40\","\
                "\"building\":\"41\",\"building_leading_type\":\"42\",\"building_name\":\"43\","\
                "\"building_trailing_type\":\"44\",\"sub_building_type\":\"45\",\"sub_building_number\":\"46\","\
                "\"sub_building_name\":\"47\",\"sub_building\":\"48\",\"level_type\":\"48.1\",\"level_number\":\"48.2\"," \
                "\"post_box\":\"49\",\"post_box_type\":\"50\"," \
                "\"post_box_number\":\"51\"},\"metadata\":{\"latitude\":52.0,\"longitude\":53.0,"\
                "\"geocode_precision\":\"54\",\"max_geocode_precision\":\"55\",\"address_format\":\"56\"},"\
                "\"analysis\":{\"verification_status\":\"57\",\"address_precision\":\"58\","\
                "\"max_address_precision\":\"59\",\"changes\":{\"organization\":\"60\","\
                "\"address1\":\"61\",\"address2\":\"62\",\"address3\":\"63\",\"address4\":\"64\",\"address5\":\"65\","\
                "\"address6\":\"66\",\"address7\":\"67\",\"address8\":\"68\",\"address9\":\"69\",\"address10\":\"70\","\
                "\"address11\":\"71\",\"address12\":\"72\",\"components\":{\"super_administrative_area\":\"73\"," \
                "\"administrative_area\":\"74\",\"administrative_area_short\":\"74.1\",\"administrative_area_long\":\"74.2\"," \
                "\"sub_administrative_area\":\"75\",\"building\":\"76\","\
                "\"dependent_locality\":\"77\",\"dependent_locality_name\":\"78\",\"double_dependent_locality\":\"79\","\
                "\"country_iso_3\":\"80\",\"locality\":\"81\",\"postal_code\":\"82\",\"postal_code_short\":\"83\","\
                "\"postal_code_extra\":\"84\",\"premise\":\"85\",\"premise_extra\":\"86\",\"premise_number\":\"87\","\
                "\"premise_type\":\"88\",\"premise_prefix_number\":\"89\",\"thoroughfare\":\"90\","\
                "\"thoroughfare_predirection\":\"91\",\"thoroughfare_postdirection\":\"92\","\
                "\"thoroughfare_name\":\"93\",\"thoroughfare_trailing_type\":\"94\",\"thoroughfare_type\":\"95\","\
                "\"dependent_thoroughfare\":\"96\",\"dependent_thoroughfare_predirection\":\"97\","\
                "\"dependent_thoroughfare_postdirection\":\"98\",\"dependent_thoroughfare_name\":\"99\","\
                "\"dependent_thoroughfare_trailing_type\":\"100\",\"dependent_thoroughfare_type\":\"101\","\
                "\"building_leading_type\":\"102\",\"building_name\":\"103\",\"building_trailing_type\":\"104\","\
                "\"sub_building_type\":\"105\",\"sub_building_number\":\"106\",\"sub_building_name\":\"107\"," \
                "\"sub_building\":\"108\",\"level_type\":\"108.1\",\"level_number\":\"108.2\","\
                "\"post_box\":\"109\",\"post_box_type\":\"110\",\"post_box_number\":\"111\",\"additional_content\":\"112\"," \
                "\"delivery_installation\":\"113\",\"delivery_installation_type\":\"114\",\"delivery_installation_qualifier_name\":\"115\"," \
                "\"route\":\"116\",\"route_number\":\"117\",\"route_type\":\"118\",\"use_indicator\":\"119\"}}}}]"

        serializer = NativeSerializer()
        candidate = Candidate(serializer.deserialize(response_payload)[0])

        self.assertEqual("12345678", candidate.input_id)
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
        self.assertEqual("16.1", components.administrative_area_iso2)
        self.assertEqual("16.2", components.administrative_area_short)
        self.assertEqual("16.3", components.administrative_area_long)
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
        self.assertEqual("27.5", components.premise_prefix_number)
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
        self.assertEqual("48.1", components.level_type)
        self.assertEqual("48.2", components.level_number)
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

        changes = analysis.changes
        self.assertIsNotNone(changes)
        self.assertEqual("60", changes.organization)
        self.assertEqual("61", changes.address1)
        self.assertEqual("62", changes.address2)
        self.assertEqual("63", changes.address3)
        self.assertEqual("64", changes.address4)
        self.assertEqual("65", changes.address5)
        self.assertEqual("66", changes.address6)
        self.assertEqual("67", changes.address7)
        self.assertEqual("68", changes.address8)
        self.assertEqual("69", changes.address9)
        self.assertEqual("70", changes.address10)
        self.assertEqual("71", changes.address11)
        self.assertEqual("72", changes.address12)

        components = changes.components
        self.assertIsNotNone(components)
        self.assertEqual("73", components.super_administrative_area)
        self.assertEqual("74", components.administrative_area)
        self.assertEqual("74.1", components.administrative_area_short)
        self.assertEqual("74.2", components.administrative_area_long)
        self.assertEqual("75", components.sub_administrative_area)
        self.assertEqual("76", components.building)
        self.assertEqual("77", components.dependent_locality)
        self.assertEqual("78", components.dependent_locality_name)
        self.assertEqual("79", components.double_dependent_locality)
        self.assertEqual("80", components.country_iso_3)
        self.assertEqual("81", components.locality)
        self.assertEqual("82", components.postal_code)
        self.assertEqual("83", components.postal_code_short)
        self.assertEqual("84", components.postal_code_extra)
        self.assertEqual("85", components.premise)
        self.assertEqual("86", components.premise_extra)
        self.assertEqual("87", components.premise_number)
        self.assertEqual("88", components.premise_type)
        self.assertEqual("89", components.premise_prefix_number)
        self.assertEqual("90", components.thoroughfare)
        self.assertEqual("91", components.thoroughfare_predirection)
        self.assertEqual("92", components.thoroughfare_postdirection)
        self.assertEqual("93", components.thoroughfare_name)
        self.assertEqual("94", components.thoroughfare_trailing_type)
        self.assertEqual("95", components.thoroughfare_type)
        self.assertEqual("96", components.dependent_thoroughfare)
        self.assertEqual("97", components.dependent_thoroughfare_predirection)
        self.assertEqual("98", components.dependent_thoroughfare_postdirection)
        self.assertEqual("99", components.dependent_thoroughfare_name)
        self.assertEqual("100", components.dependent_thoroughfare_trailing_type)
        self.assertEqual("101", components.dependent_thoroughfare_type)
        self.assertEqual("102", components.building_leading_type)
        self.assertEqual("103", components.building_name)
        self.assertEqual("104", components.building_trailing_type)
        self.assertEqual("105", components.sub_building_type)
        self.assertEqual("106", components.sub_building_number)
        self.assertEqual("107", components.sub_building_name)
        self.assertEqual("108", components.sub_building)
        self.assertEqual("108.1", components.level_type)
        self.assertEqual("108.2", components.level_number)
        self.assertEqual("109", components.post_box)
        self.assertEqual("110", components.post_box_type)
        self.assertEqual("111", components.post_box_number)
        self.assertEqual("112", components.additional_content)
        self.assertEqual("113", components.delivery_installation)
        self.assertEqual("114", components.delivery_installation_type)
        self.assertEqual("115", components.delivery_installation_qualifier_name)
        self.assertEqual("116", components.route)
        self.assertEqual("117", components.route_number)
        self.assertEqual("118", components.route_type)
        self.assertEqual("119", components.use_indicator)
