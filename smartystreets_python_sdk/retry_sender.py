from time import sleep


class RetrySender:
    def __init__(self, maxretries, inner):
        self.inner = inner
        self.maxretries = maxretries
        self.MAX_BACKOFF_DURATION = 10

    def send(self, request):
        if self.maxretries == 0:
            return self.inner.send(request)

        for i in range(self.maxretries):
            response = self.inner.send(request)

            if response.status_code == 200:
                break

            self.backoff(i)

        return response

    def backoff(self, attempt):
        sleep(min_duration(attempt, self.MAX_BACKOFF_DURATION))
        return

    """
    def trysend(self, request, attempt):
        response = self.inner.send(request)

        if response.status_code != 200 and attempt >= self.maxretries:
            return response

        return None
    """


def min_duration(a, b):
    if a < b:
        return a
    return b
