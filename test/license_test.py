import unittest
import smartystreets_python_sdk as smarty
from test.mocks import *


class TestLicenseSender(unittest.TestCase):

    def test_license_set(self):
        sender = MockSender(None)
        licenses = ['one', 'two', 'three']
        sender = smarty.LicenseSender(licenses, sender)
        request = smarty.Request()
        request.url_prefix = "http://localhost"

        sender.send(request)

        self.assertEqual('one,two,three', request.parameters['license'])

    def test_license_not_set(self):
        sender = MockSender(None)
        sender = smarty.LicenseSender([], sender)
        request = smarty.Request()
        request.url_prefix = "http://localhost"

        sender.send(request)

        self.assertEqual(0, len(request.parameters))
