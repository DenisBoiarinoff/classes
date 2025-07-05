class ProductMixinLog:

    def __init__(self):
        print(f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})")
