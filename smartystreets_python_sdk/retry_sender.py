from time import sleep


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


def min_duration(a, b):
    if a < b:
        return a
    return b


def backoff(attempt):
    sleep(min_duration(attempt, RetrySender.MAX_BACKOFF_DURATION))
    return
