from time import sleep

import sys


class RetrySender:
    MAX_BACKOFF_DURATION = 10
    STATUS_OK = 200
    TOO_MANY_REQUESTS = 429

    def __init__(self, max_retries, inner):
        self.inner = inner
        self.max_retries = max_retries

    def send(self, request):
        response = self.inner.send(request)

        for i in range(self.max_retries):
            if response.status_code == RetrySender.STATUS_OK:
                break

            if response.status_code == RetrySender.TOO_MANY_REQUESTS:
                backoff_seconds = 10
                retry_after = response.getHeader("Retry-After")

                if retry_after is not None:
                    backoff_seconds = int(retry_after)

                backoff(backoff_seconds, True)
            else:
                backoff(i)

            response = self.inner.send(request)

        return response


def backoff(attempt, ignore_max=False):
    max_backoff = RetrySender.MAX_BACKOFF_DURATION
    if ignore_max:
        max_backoff = attempt
    print("There was an error processing the request. Retrying in {} seconds...".format(
        min(attempt, max_backoff)), file=sys.stderr)
    sleep(min(attempt, max_backoff))
    return
