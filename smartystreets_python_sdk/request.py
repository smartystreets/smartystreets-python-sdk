from collections import OrderedDict


class Request:
    def __init__(self, urlprefix=None):
#        self.headers = OrderedDict()
        self.parameters = OrderedDict()
        self.payload = None
        self.urlprefix = urlprefix
#        self.method = "GET"  # Is this helpful?

    """
    def putheader(self, name, value):
        self.headers[name] = value


    def putparameter(self, name, value):
        if name is None or value is None or len(name) == 0:
            return

        self.parameters[name] = value

    def urlencode(self, value):
        return value

    def geturl(self):
        url = self.urlprefix

        if "?" not in url:
            url += "?"

        for value in self.parameters:
            if not url.endswith("?"):
                url += "&"

            encodedname = self.urlencode(value)
            encodedvalue = self.urlencode(self.parameters[value])
            url += encodedname + "=" + encodedvalue

        return url
"""
