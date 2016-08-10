class MockSender:
    def __init__(self, response):
        self.response = response
        self.request = None

    def send(self, request):
        self.request = request
        return self.response
