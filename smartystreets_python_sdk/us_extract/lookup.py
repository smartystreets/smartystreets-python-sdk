from smartystreets_python_sdk.us_extract import Result


class Lookup:
    def __init__(self, text=None, html=None, aggressive=False, addresses_have_line_breaks=True, addresses_per_line=0):
        self.result = Result()
        self.text = text
        self.html = html
        self.aggressive = aggressive
        self.addresses_have_line_breaks = addresses_have_line_breaks
        self.addresses_per_line = addresses_per_line

