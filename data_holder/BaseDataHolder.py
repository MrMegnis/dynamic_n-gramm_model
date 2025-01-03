from abc import ABC, abstractmethod
from typing import List, Dict


class BaseDataHolder(ABC):
    """
    Class for store, load, save and get data for model's predictions.
    Storage should contain for each context (list of tokens) amount of tokens that models saw
    with that context.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Init method. Contain steps for connecting to storage or other important code."""
        pass

    @abstractmethod
    def add(self, context_sequence: List[int], token: int) -> None:
        """Add in storage context with following token."""
        pass

    @abstractmethod
    def __getitem__(self, context: List[int]) -> Dict[int, int]:
        """Get context (list of tokens) and return list of tuples - token and it's amount"""
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        """Save data in dataholder"""
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        """Load data to dataholder"""
        pass
