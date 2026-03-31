import json

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
        self.input_id = obj.get('input_id', None)
        self.input_index = obj.get('input_index', None)
        self.candidate_index = obj.get('candidate_index', None)
        self.addressee = obj.get('addressee', None)
        self.delivery_line_1 = obj.get('delivery_line_1', None)
        self.delivery_line_2 = obj.get('delivery_line_2', None)
        self.last_line = obj.get('last_line', None)
        self.delivery_point_barcode = obj.get('delivery_point_barcode', None)
        self.smarty_key = obj.get('smarty_key', None)
        self.smarty_key_ext = obj.get('smarty_key_ext', None)
        self.components = Components(obj.get('components', {}))
        self.metadata = Metadata(obj.get('metadata', {}))
        self.analysis = Analysis(obj.get('analysis', {}))

    def to_dict(self):
        components_dict = self.components.to_dict() if self.components else None
        metadata_dict = self.metadata.to_dict() if self.metadata else None
        analysis_dict = self.analysis.to_dict() if self.analysis else None

        result = {
            "input_id": self.input_id,
            "input_index": self.input_index,
            "candidate_index": self.candidate_index,
            "addressee": self.addressee,
            "delivery_line_1": self.delivery_line_1,
            "delivery_line_2": self.delivery_line_2,
            "last_line": self.last_line,
            "delivery_point_barcode": self.delivery_point_barcode,
            "smarty_key": self.smarty_key,
            "smarty_key_ext": self.smarty_key_ext,
            "components": components_dict or None,
            "metadata": metadata_dict or None,
            "analysis": analysis_dict or None
        }
        return {k: v for k, v in result.items() if v is not None}

    def to_json(self):
        return json.dumps(self.to_dict())