class Batch:
    MAX_BATCH_SIZE = 100

    def __init__(self):
        self.named_lookups = {}
        self.all_lookups = []

    def __getitem__(self, item):
        return self.all_lookups[item]

    def add(self, lookup):
        if self.isfull():
            return False

        self.all_lookups.append(lookup)

        if lookup.input_id is None:
            return True

        self.named_lookups[lookup.input_id] = lookup

        return True

    def clear(self):
        self.named_lookups.clear()
        self.all_lookups = []

    def size(self):
        return len(self.all_lookups)

    def isfull(self):
        return self.size() >= Batch.MAX_BATCH_SIZE

    def get_by_input_id(self, input_id):
        return self.named_lookups[input_id]
