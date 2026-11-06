from abc import ABC, abstractmethod
from classes.supplier import Supplier

class Product(ABC):
    def __init__(self, id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__id: str = id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    def display_information(self) -> None:
        print(f'ID: {self.__id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}', end="")

    def display_detailed_information(self) -> None:
        print("------------------------------------------------")
        print(f'ID: {self.__id}')
        print(f'Name: {self.__name}')
        print(f'Price: ${self.__price:.2f}')
        print(f'Stock: {self.__stock}')
        print("------------------------------------------------")

    def display_supplier_information(self) -> None:
        self.__supplier.display_information()

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_stock(self) -> int:
        return self.__stock

    def get_price(self) -> float:
        return self.__price

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
