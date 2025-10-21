import unittest
import smartystreets_python_sdk as smarty
from test.mocks import *


class TestCustomQuerySender(unittest.TestCase):
    def test_custom_queries_set(self):
        sender = MockSender(None)
        custom_queries = {'one': '1,won,one', 'two': '2', 'three': '3'}
        sender = smarty.CustomQuerySender(custom_queries, sender)
        request = smarty.Request()
        request.url_prefix = "http://localhost"

        sender.send(request)

        self.assertEqual('1,won,one', request.parameters['one'])
        self.assertEqual('2', request.parameters['two'])
        self.assertEqual('3', request.parameters['three'])
    
    def test_custom_queries_not_set(self):
        sender = MockSender(None)
        sender = smarty.CustomQuerySender({}, sender)
        request = smarty.Request()
        request.url_prefix = "http://localhost"

        sender.send(request)

        self.assertEqual(0, len(request.parameters))

    def test_custom_queries_none(self):
        sender = MockSender(None)
        sender = smarty.CustomQuerySender(None, sender)
        request = smarty.Request()
        request.url_prefix = "http://localhost"

        sender.send(request)

        self.assertEqual(0, len(request.parameters))