from collections import OrderedDict


class Request:
    def __init__(self):
        self.parameters = OrderedDict()
        self.payload = None
        self.url_prefix = None
        self.referer = None
        self.content_type = 'application/json'
