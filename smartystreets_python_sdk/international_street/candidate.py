from .components import Components
from .metadata import Metadata
from .analysis import Analysis


class Candidate:
    def __init__(self, obj):
        """
        A candidate is a possible match for an address that was submitted. A lookup can have multiple 
        candidates if the address was ambiguous.
        
        See "https://smartystreets.com/docs/cloud/international-street-api#root"
        """
        self.organization = obj.get("organization", None)
        self.address1 = obj.get("address1", None)
        self.address2 = obj.get("address2", None)
        self.address3 = obj.get("address3", None)
        self.address4 = obj.get("address4", None)
        self.address5 = obj.get("address5", None)
        self.address6 = obj.get("address6", None)
        self.address7 = obj.get("address7", None)
        self.address8 = obj.get("address8", None)
        self.address9 = obj.get("address9", None)
        self.address10 = obj.get("address10", None)
        self.address11 = obj.get("address11", None)
        self.address12 = obj.get("address12", None)
        self.components = Components(obj.get("components", {}))
        self.metadata = Metadata(obj.get("metadata", {}))
        self.analysis = Analysis(obj.get("analysis", {}))
