"""module with PrintMixin class definition"""


class PrintMixin:
    """
    implementing printing of class and parameters for created object
    requires properly defined __repr__ method in class
    """

    def __init__(self) -> None:
        print(repr(self))
