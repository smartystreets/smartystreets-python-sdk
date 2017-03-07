class Lookup:
    def __init__(self, text=None, html=None, aggressive=None, addresses_have_line_breaks=None, addresses_per_line=None):
        self.result = None
        self.text = text
        self.html = html
        self.aggressive = aggressive
        self.addresses_have_line_breaks = addresses_have_line_breaks
        self.addresses_per_line = addresses_per_line

