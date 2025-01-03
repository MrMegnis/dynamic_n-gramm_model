from abc import ABC, abstractmethod
from data_holder import BaseDataHolder
from typing import Any, Dict, List


class BaseNGramModel(ABC):
    @abstractmethod
    def __init__(self, n: int, data_holder: BaseDataHolder) -> None:
        pass

    @abstractmethod
    def predict(self, context_sequence: Any) -> Dict[int, int]:
        pass

    @abstractmethod
    def update(self, tokens: List[int]) -> None:
        pass

    @abstractmethod
    def save(self, path: str):
        """Save model"""
        pass

    @abstractmethod
    def load(self, path: str):
        """Load model"""
        pass
