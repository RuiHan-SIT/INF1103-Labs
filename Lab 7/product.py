from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, id: str, name: str, price: float, stock: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(f'ID: {self.__id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}', end="")

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

    @abstractmethod
    def get_fulfilment_info(self):
        pass
