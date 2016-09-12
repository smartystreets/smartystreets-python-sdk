from collections import OrderedDict


class Request:
    def __init__(self):
        self.parameters = OrderedDict()
        self.payload = None
        self.urlprefix = None
