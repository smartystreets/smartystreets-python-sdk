from .components import Components
from .metadata import Metadata
from .analysis import Analysis


class Candidate:
    def __init__(self, obj):
        """
        A candidate is a possible match for an address that was submitted.
        A lookup can have multiple candidates if the address was ambiguous, and
        the maxCandidates field is set higher than 1.

        See "https://smartystreets.com/docs/cloud/us-street-api#root"
        """
        self.input_index = obj.get('input_index', None)
        self.candidate_index = obj.get('candidate_index', None)
        self.addressee = obj.get('addressee', None)
        self.delivery_line_1 = obj.get('delivery_line_1', None)
        self.delivery_line_2 = obj.get('delivery_line_2', None)
        self.last_line = obj.get('last_line', None)
        self.delivery_point_barcode = obj.get('delivery_point_barcode', None)
        self.components = Components(obj.get('components', {}))
        self.metadata = Metadata(obj.get('metadata', {}))
        self.analysis = Analysis(obj.get('analysis', {}))
