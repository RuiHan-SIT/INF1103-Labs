from classes.product import Product

class Inventory:
    def __init__(self):
        self.__inventory: list[Product] = []

    def add_product(self, product: Product):
        self.__inventory.append(product)

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------------------------------------------------------")
        for product in self.__inventory:
            product.display_information()
        print("------------------------------------------------------------------------------------------------")

    def search_product(self, id: str) -> Product | None:
        for product in self.__inventory:
            if id == product.get_id():
                return product
        return None

    def remove_product(self, id: str):
        for product in self.__inventory:
            if id == product.get_id():
                self.__inventory.remove(product)
                break

    def get_products(self):
        return self.__inventory