from .components import Components
from .rootlevel import RootLevel

class Changes(RootLevel):
    def __init__(self, obj):
        RootLevel.__init__(self, obj)
        self.components = Components(obj.get("components", {}))
