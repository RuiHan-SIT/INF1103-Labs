from classes.product import Product
from classes.can_be_shipped import CanBeShipped
from classes.supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(id, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f" | Weight: {self.__weight:.2f}kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_cost = self.__weight * 2
        return shipping_cost

    def to_dict(self) -> dict:
        data = {"type": "physical"}
        data.update(super().to_dict())
        data["weight"] = self.__weight
        return data
