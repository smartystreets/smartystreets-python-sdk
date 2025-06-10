class MatchInfo:
    def __init__(self, obj):
        """
        Holds matching status and change information for an address component.
        """
        self.status = obj.get('status', None)
        self.change = obj.get('change', None)