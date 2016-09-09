import unittest
from smartystreets_python_sdk import Request, RetrySender


class TestRetrySender(unittest.TestCase):

    def test_success_does_not_retry(self):
        pass


def send_with_retry(retries, inner):
    request = Request("test")
    retrysender = RetrySender(retries, inner)
    return retrysender.send(request)
