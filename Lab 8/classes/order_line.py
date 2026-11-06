from classes.product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product_id(self) -> str:
        return self.__product.get_id()

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        subtotal = self.__product.get_price() * self.__quantity
        return subtotal

    def display_information(self) -> None:
        print(f"{self.__product.get_id()} | {self.__product.get_name()} | Quantity: {self.__quantity} | Subtotal: ${self.calculate_subtotal():.2f}")
