import unittest
from smartystreets_python_sdk import Request, RetrySender


class TestRetrySender(unittest.TestCase):
    def __init__(self):
        self.mocksender = None

    def test_success_does_not_retry(self):
        pass

    def send_request(self, request_behavior):
        request = Request(request_behavior)
        retrysender = RetrySender(5, self.mocksender)
