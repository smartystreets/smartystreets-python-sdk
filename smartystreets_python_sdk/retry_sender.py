from time import sleep


class RetrySender:
    MAX_BACKOFF_DURATION = 10

    def __init__(self, max_retries, inner):
        self.inner = inner
        self.max_retries = max_retries

    def send(self, request):
        if self.max_retries == 0:
            return self.inner.send(request)

        for i in range(self.max_retries):
            response = self.inner.send(request)

            if response.status_code == 200:
                break

            self.backoff(i)

        return response

    def backoff(self, attempt):
        sleep(min_duration(attempt, RetrySender.MAX_BACKOFF_DURATION))
        return


def min_duration(a, b):
    if a < b:
        return a
    return b
