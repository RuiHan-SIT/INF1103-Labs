from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f" | Weight: {self.__weight:.2f}kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        shipping_cost = self.__weight * 2
        return shipping_cost

    def to_dict(self):
        data = {"type": "physical"}
        data.update(super().to_dict())
        data["weight"] = self.__weight
        return data
