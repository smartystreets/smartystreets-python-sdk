class MatchInfo:
    def __init__(self, obj: dict) -> None:
        """
        Holds matching status and change information for an address component.
        """
        self.status: str | None = obj.get('status', None)
        self.change: list[str] | None = obj.get('change', None)

    def to_dict(self) -> dict:
        result = {
            "status": self.status,
            "change": self.change
        }
        return {k: v for k, v in result.items() if v is not None}