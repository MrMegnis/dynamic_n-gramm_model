from models import BaseNGramModel
from data_holder import BaseDataHolder
from tokenizers import BaseTokenizer


class DynamicNGramModel(BaseNGramModel):
    def __init__(self, n: int, data_holder: BaseDataHolder, tokenizer: BaseTokenizer) -> None:
        self.n = n
        self.data_holder = data_holder
        self.tokenizer = tokenizer

    def predict(self, context_sequence: str):
        preprocessed_sequence = context_sequence.strip().split()
        tokenize_sequence = self.tokenizer.sequence2tokens(preprocessed_sequence)
        predictions = self.data_holder[tokenize_sequence]
        total = sum(predictions.values())
        probabilities = {token: count / total for token, count in predictions.items()}
        return probabilities

    def update(self, sequence: str):
        preprocessed_sequence = sequence.strip().split()
        self.tokenizer.add_items(preprocessed_sequence)
        tokenize_sequence = self.tokenizer.sequence2tokens(preprocessed_sequence)
        for i in range(len(tokenize_sequence) - self.n + 1):
            context = tokenize_sequence[i:i + self.n - 1]
            next_word = tokenize_sequence[i + self.n - 1]
            self.data_holder.add(context, next_word)

    def save(self, path: str):
        pass

    def load(self, path: str):
        pass
