"""module with BaseProduct class definition"""

from abc import ABC, abstractmethod


class ProductsGroup(ABC):
    """abstract class to represent a base products group"""

    @property
    @abstractmethod
    def products(self) -> str:
        """group products in string format"""
