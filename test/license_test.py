import unittest
import smartystreets_python_sdk as smarty


class TestLicenseSender(unittest.TestCase):

    def test_license_set(self):
        sender = smarty.RequestsSender()
        licenses = ['one', 'two', 'three']
        sender = smarty.LicenseSender(licenses, sender)
        request = smarty.Request()
        request.url_prefix = "http://localhost"

        sender.send(request)

        self.assertEqual('one,two,three', request.parameters['licenses'])

    def test_license_not_set(self):
        sender = smarty.RequestsSender()
        sender = smarty.LicenseSender([], sender)
        request = smarty.Request()
        request.url_prefix = "http://localhost"

        sender.send(request)

        self.assertEqual(0, len(request.parameters))
