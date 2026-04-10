from src.category import Category


class ProductIterator:

    def __init__(self, product_category: Category) -> None:
        self.__products_list = product_category.products_list
        self.__index = 0

    def __iter__(self) -> ProductIterator:
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__products_list):
            product = self.__products_list[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration

    @property
    def index(self) -> int:
        return self.__index
