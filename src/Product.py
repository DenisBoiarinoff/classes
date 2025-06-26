class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params: dict):
        return Product(
            params["name"],
            params["description"],
            params["price"],
            params["quantity"]
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = price
