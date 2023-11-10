import unittest

from smartystreets_python_sdk import URLPrefixSender
from smartystreets_python_sdk import Request 

class TestURLPrefixSender(unittest.TestCase):
    def test_request_url_present(self):
        fakeSender = FakeSender()
        prefix_sender = URLPrefixSender('https://mysite.com', fakeSender)
        request = Request()
        request.url_prefix = '/jimbo'

        new_request = prefix_sender.send(request)
        self.assertEqual('https://mysite.com/jimbo', new_request.url_prefix)

    def test_request_url_not_present(self):
        fakeSender = FakeSender()
        prefix_sender = URLPrefixSender('https://mysite.com', fakeSender)
        request = Request()

        new_request = prefix_sender.send(request)
        self.assertEqual('https://mysite.com', new_request.url_prefix)

class FakeSender:
    def send(self, request):
        return request