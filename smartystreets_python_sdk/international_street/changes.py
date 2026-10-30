from .components import Components
from .rootlevel import RootLevel

class Changes(RootLevel):
    def __init__(self, obj: dict) -> None:
        RootLevel.__init__(self, obj)
        self.components: Components = Components(obj.get("components", {}))
