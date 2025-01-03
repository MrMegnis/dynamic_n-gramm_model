from data_holder import BaseDataHolder
from collections import defaultdict, Counter

class DictDataHolder(BaseDataHolder):
    def __init__(self):
        self.data_holder = defaultdict(Counter)

    def add(self, context_sequence, token):
        self.data_holder[tuple(context_sequence)][token] += 1

    def __getitem__(self, item):
        return self.data_holder[tuple(item)]

    def save(self, path: str) -> None:
        pass

    def load(self, path: str) -> None:
        pass
