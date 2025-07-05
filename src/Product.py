from src.BaseProduct import BaseProduct
from src.ProductMixinLog import ProductMixinLog


class Product(ProductMixinLog, BaseProduct):

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        lhtype = type(self)
        rhtype = type(other)
        if lhtype == rhtype:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError()

    @classmethod
    def new_product(cls, params: dict):
        return Product(params["name"], params["description"], params["price"], params["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = price
