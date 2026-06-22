class Suggestion:
    def __init__(self, obj=None):
        """
        See "https://www.smarty.com/docs/apis/us-autocomplete-v2/reference#http-response-status"
        """
        self.smarty_key = obj.get('smarty_key', None)
        self.entry_id = obj.get('entry_id', None)
        self.street_line = obj.get('street_line', None)
        self.secondary = obj.get('secondary', None)
        self.city = obj.get('city', None)
        self.state = obj.get('state', None)
        self.zipcode = obj.get('zipcode', None)
        self.entries = obj.get('entries', None)
        self.source = obj.get('source', None)
