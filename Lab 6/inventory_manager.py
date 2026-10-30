import json

class Product:
    def __init__(self, id: str, name: str, price: float, stock: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(f'ID: {self.__id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}')

    def display_detailed_information(self):
        print("------------------------------------------------")
        print(f'ID: {self.__id}')
        print(f'Name: {self.__name}')
        print(f'Price: ${self.__price:.2f}')
        print(f'Stock: {self.__stock}')
        print("------------------------------------------------")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_stock(self):
        return self.__stock

    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

class Inventory:
    def __init__(self):
        self.__inventory = []

    def add_product(self, product):
        self.__inventory.append(product)

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")
        for product in self.__inventory:
            product.display_information()
        print("------------------------------------------------")

    def search_product(self, id):
        for product in self.__inventory:
            if id == product.get_id():
                return product
        return None

    def get_products(self):
        return self.__inventory
      