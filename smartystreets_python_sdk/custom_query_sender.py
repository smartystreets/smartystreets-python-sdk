class CustomQuerySender:
    def __init__(self, custom_queries, inner):
        self.custom_queries = custom_queries
        self.inner = inner

    def send(self, request):
        if self.custom_queries is not None:
            for key, value in self.custom_queries.items():
                request.parameters[key] = value
        return self.inner.send(request)