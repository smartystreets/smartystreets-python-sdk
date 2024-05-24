import smartystreets_python_sdk as smarty
import unittest


class TestCustomHeaderSender(unittest.TestCase):

    def test_populates_headers(self):
        sender = smarty.RequestsSender()
        header = {'Test-User-Agent': 'Test-Agent', 'Test-Content-Type': 'Test-Content-Type'}
        sender = smarty.CustomHeaderSender(header, sender)

        self.assertEqual(sender.headers['Test-User-Agent'], 'Test-Agent')
        self.assertEqual(sender.headers['Test-Content-Type'], 'Test-Content-Type')

    def test_custom_headers_set(self):
        sender = smarty.RequestsSender
        header = {'Test-User-Agent': 'Test-Agent', 'Test-Content-Type': 'Test-Type'}
        sender = smarty.CustomHeaderSender(header, sender)
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        request = sender.build_request(smartyrequest)

        self.assertEqual('Test-Agent', request.headers['Test-User-Agent'])
        self.assertEqual('Test-Type', request.headers['Test-Content-Type'])

    def test_custom_headers_used(self):
        sender = smarty.RequestsSender()
        header = {'User-Agent': 'Test-Agent', 'Content-Type': 'Test-Type'}
        sender = smarty.CustomHeaderSender(header, sender)
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://localhost"
        smartyrequest.payload = "This is the test content."

        request = sender.build_request(smartyrequest)
        
        # request = smarty.requests_sender.build_request(request)

        request = smarty.RequestsSender.build_request(request)

        self.assertEqual('Test-Agent', request.headers['User-Agent'])
        self.assertEqual('Test-Type', request.headers['Content-Type'])
