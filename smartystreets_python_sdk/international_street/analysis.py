class Analysis:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/international-street-api#analysis"
        """
        self.verification_status = obj.get('verification_status')
        self.address_precision = obj.get('address_precision')
        self.max_address_precision = obj.get('max_address_precision')
