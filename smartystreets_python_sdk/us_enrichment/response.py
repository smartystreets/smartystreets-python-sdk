class Response:
    def __init__(self, obj):
        self.smarty_key = obj.get('smarty_key', None)
        self.data_set_name = obj.get('data_set_name', None)
        self.data_subset_name = obj.get('data_subset_name', None)
        self.attributes = obj.get('attributes', None)

    def __str__(self):
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += '{}: {}'.format(key, val).split('\n')
        return '\n    '.join(lines)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, type(self)) and __value.smarty_key == self.smarty_key