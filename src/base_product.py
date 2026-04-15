"""module with BaseProduct class definition"""

from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """abstract class to represent a base product"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """create an instance of a some product"""

    @property
    @abstractmethod
    def price(self) -> float:
        """price of a product"""
