from .components import Components
from .metadata import Metadata
from .analysis import Analysis
from .rootlevel import RootLevel

class Candidate(RootLevel):
    def __init__(self, obj):
        """
        A candidate is a possible match for an address that was submitted. A lookup can have multiple 
        candidates if the address was ambiguous.
        
        See "https://smartystreets.com/docs/cloud/international-street-api#root"
        """
        RootLevel.__init__(self, obj)
        self.components = Components(obj.get("components", {}))
        self.metadata = Metadata(obj.get("metadata", {}))
        self.analysis = Analysis(obj.get("analysis", {}))
