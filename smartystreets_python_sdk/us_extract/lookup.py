class Lookup:
    def __init__(self, input =None,html=False, aggressive=False, addr_line_breaks=True, addr_per_line=0, input_id=None):
        self.result = []
        self.input_id = input_id
        self.input = input
        self.html = html
        self.aggressive = aggressive
        self.addr_line_breaks = addr_line_breaks
        self.addr_per_line = addr_per_line
