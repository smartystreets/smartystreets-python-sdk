class MatchInfo:
    def __init__(self, obj):
        """
        Holds matching status and change information for an address component.
        """
        self.status = obj.get('status', None)
        self.change = obj.get('change', None)

    def to_dict(self):
        result = {
            "status": self.status,
            "change": self.change
        }
        return {k: v for k, v in result.items() if v is not None}