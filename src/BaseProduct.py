from abc import abstractmethod, ABC


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, price: float):
        pass
