from classes.product import Product
from classes.supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, id: str, name: str, price: float, stock: int, download_size: int, supplier: Supplier):
        super().__init__(id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f" | Download Size: {self.__download_size}MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = {"type": "digital"}
        data.update(super().to_dict())
        data["download_size"] = self.__download_size
        return data
