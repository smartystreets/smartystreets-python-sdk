class Address:
    def __init__(self, obj):
        self.candidate_index = (obj.get('api_output', [{}])[:1] or [{}])[0].get('candidate_index', 0)
        self.input_index = (obj.get('api_output', [{}])[:1] or [{}])[0].get('input_index', 0)
        self.text = obj.get('text', None)
        self.verified = obj.get('verified', None)
        self.line = obj.get('line', None)
        self.start = obj.get('start', None)
        self.end = obj.get('end', None)
