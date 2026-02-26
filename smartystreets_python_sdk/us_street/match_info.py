class MatchInfo:
    def __init__(self, obj):
        """
        Holds matching status and change information for an address component.
        """
        self.status = obj.get('status', None)
        self.change = obj.get('change', None)

    def to_dict(self):
        return {"status": self.status, **({"change": self.change} if self.change is not None else {})}