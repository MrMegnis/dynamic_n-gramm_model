from abc import ABC, abstractmethod
from typing import List, Any


class BaseTokenizer(ABC):
    """
    Class for sequence tokenization. Can encode and decode sequence to list of tokens
    """

    @abstractmethod
    def __init__(self, max_vocab) -> None:
        """Init method. Contain steps for vocab setup"""
        pass

    @abstractmethod
    def item2token(self, item: Any) -> int:
        """Encode one item to token"""
        pass

    @abstractmethod
    def token2item(self, token: int) -> Any:
        """Decode one token to item"""
        pass

    @abstractmethod
    def sequence2tokens(self, items_list: List[Any]) -> List[int]:
        """Encode sequence of items to list of token"""
        pass

    @abstractmethod
    def tokens2sequence(self, tokens_list: List[int]) -> List[Any]:
        """Decode list of token to sequence of items"""
        pass

    def add_items(self, items_list: List[Any]):
        """"""
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        """Save tokenizer"""
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        """Load tokenizer"""
        pass
