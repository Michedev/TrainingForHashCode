class Product:
    def __init__(self, type: int, weight : int):
        self.type, self.weight = type, weight

    def __eq__(self, other):
        if isinstance(other, Product) :
            return other.type == self.type