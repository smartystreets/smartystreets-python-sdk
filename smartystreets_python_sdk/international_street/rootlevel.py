class RootLevel:
    def __init__(self, obj: dict) -> None:
        self.input_id: str | None = obj.get("input_id", None)
        self.organization: str | None = obj.get("organization", None)
        self.address1: str | None = obj.get("address1", None)
        self.address2: str | None = obj.get("address2", None)
        self.address3: str | None = obj.get("address3", None)
        self.address4: str | None = obj.get("address4", None)
        self.address5: str | None = obj.get("address5", None)
        self.address6: str | None = obj.get("address6", None)
        self.address7: str | None = obj.get("address7", None)
        self.address8: str | None = obj.get("address8", None)