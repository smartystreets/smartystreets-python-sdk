import unittest
from smartystreets_python_sdk import Request, RetrySender
from mock import patch
from .mocks import FailingSender


def mock_backoff(attempt, ignore_max=False):
    TestRetrySender.sleep_durations.append(min(attempt, 10))


class TestRetrySender(unittest.TestCase):
    sleep_durations = []

    def setUp(self):
        TestRetrySender.sleep_durations = []

    @patch('smartystreets_python_sdk.retry_sender.backoff', side_effect=mock_backoff)
    def test_success_does_not_retry(self, mocked):
        inner = FailingSender([200])

        send_with_retry(5, inner)

        self.assertEqual(1, inner.current_status_code_index)

    @patch('smartystreets_python_sdk.retry_sender.backoff', side_effect=mock_backoff)
    def test_retry_until_success(self, mocked):
        inner = FailingSender([408, 500, 502, 200, 504])

        send_with_retry(10, inner)

        self.assertEqual(4, inner.current_status_code_index)

    @patch('smartystreets_python_sdk.retry_sender.backoff', side_effect=mock_backoff)
    def test_return_response_if_retry_limit_exceeded(self, mocked):
        inner = FailingSender([500, 500, 500, 500, 500, 500])

        response = send_with_retry(4, inner)

        self.assertIsNotNone(response)
        self.assertEqual(5, inner.current_status_code_index)
        self.assertEqual([0,1,2,3], TestRetrySender.sleep_durations)
        self.assertEqual(500, response.status_code)

    @patch('smartystreets_python_sdk.retry_sender.backoff', side_effect=mock_backoff)
    def test_backoff_does_not_exceed_max(self, mocked):
        inner = FailingSender([408, 408, 408, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 200])

        send_with_retry(20, inner)

        self.assertEqual([0,1,2,3,4,5,6,7,8,9,10,10,10], TestRetrySender.sleep_durations)

    @patch('smartystreets_python_sdk.retry_sender.backoff', side_effect=mock_backoff)
    def test_sleep_on_rate_limit(self, mocked):
        inner = FailingSender([429, 200])

        send_with_retry(1, inner)

        self.assertEqual([10], TestRetrySender.sleep_durations)

    @patch('smartystreets_python_sdk.retry_sender.backoff', side_effect=mock_backoff)
    def test_sleep_on_rate_limit_error(self, mocked):
        inner = FailingSender([429, 200], "Big bad")

        response = send_with_retry(1, inner)

        self.assertEqual(response.error, "Big bad")



def send_with_retry(retries, inner):
    request = Request()
    sender = RetrySender(retries, inner)
    return sender.send(request)



