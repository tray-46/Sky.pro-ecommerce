"""module with BaseProduct class definition"""

from abc import ABC, abstractmethod
from typing import Generic, ParamSpec

P = ParamSpec("P")


class BaseProduct(ABC, Generic[P]):
    """abstract class to represent a base product"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: P.args, **kwargs: P.kwargs) -> BaseProduct:
        """create an instance of a some product"""

    @property
    @abstractmethod
    def price(self) -> float:
        """price of a product"""
