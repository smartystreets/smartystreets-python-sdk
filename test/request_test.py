import smartystreets_python_sdk as smarty
import unittest


class TestRequest(unittest.TestCase):
    """
    def test_null_name_query_string_parameter_not_added(self):
        self.assert_query_string_parameters(None, "value", "http://localhost/?")

    def test_empty_name_query_string_parameter_not_added(self):
        self.assert_query_string_parameters("", "value", "http://localhost/?")

    def test_null_value_query_string_parameter_not_added(self):
        self.assert_query_string_parameters("name", None, "http://localhost/?")

    def test_empty_value_query_string_parameter_is_added(self):
        self.assert_query_string_parameters("name", "", "http://localhost/?name=")

    def assert_query_string_parameters(self, name, value, expected):
        request = smarty.Request("http://localhost/?")

        request.putparameter(name, value)

        self.assertEqual(expected, request.geturl())


    def test_multiple_query_string_parameters(self):
        request = smarty.Request("http://localhost/?")

        request.putparameter("name1", "value1")
        request.putparameter("name2", "value2")
        request.putparameter("name3", "value3")

        expected = "http://localhost/?name1=value1&name2=value2&name3=value3"
        self.assertEqual(expected, request.geturl())

    def testUrlEncodingOfQueryStringParameters(self):
        request = smarty.Request("http://localhost/?")

        request.putparameter("name&", "value")
        request.putparameter("name1", "other !value$")

        expected = "http://localhost/?name%26=value&name1=other+%21value%24"

        self.assertEqual(expected, request.geturl())
    """
