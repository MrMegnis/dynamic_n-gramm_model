from tokenizers import BaseTokenizer


class SimpleTokenizer(BaseTokenizer):
    def __init__(self, max_vocab) -> None:
        self.item2token_vocab = dict()
        self.token2item_vocab = dict()

    def item2token(self, item):
        return self.item2token_vocab[item]

    def token2item(self, token):
        return self.token2item_vocab[token]

    def sequence2tokens(self, items_list):
        return [self.item2token(item) for item in items_list]

    def tokens2sequence(self, tokens_list):
        return [self.token2item(token) for token in tokens_list]

    def add_items(self, items_list: list):
        for item in items_list:
            if not (item in self.item2token_vocab or item in list(self.token2item_vocab.values())):
                self.item2token_vocab[item] = len(self.item2token_vocab)
                self.token2item_vocab[len(self.token2item_vocab)] = item
            elif (item in self.item2token_vocab and item not in self.token2item_vocab) or (
                    item not in self.item2token_vocab and item in self.token2item_vocab):
                pass #raise Exception

    def save(self, path: str) -> None:
        pass

    def load(self, path: str) -> None:
        pass
