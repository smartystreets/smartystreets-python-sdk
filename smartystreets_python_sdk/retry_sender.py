from time import sleep

import sys


class RetrySender:
    MAX_BACKOFF_DURATION = 10
    STATUS_OK = 200

    def __init__(self, max_retries, inner):
        self.inner = inner
        self.max_retries = max_retries

    def send(self, request):
        response = self.inner.send(request)

        for i in range(self.max_retries):
            if response.status_code == RetrySender.STATUS_OK:
                break

            backoff(i)

            response = self.inner.send(request)

        return response


def backoff(attempt):
    print("There was an error processing the request. Retrying in {} seconds...".format(
        min(attempt, RetrySender.MAX_BACKOFF_DURATION)), sys.stderr)
    sleep(min(attempt, RetrySender.MAX_BACKOFF_DURATION))
    return
