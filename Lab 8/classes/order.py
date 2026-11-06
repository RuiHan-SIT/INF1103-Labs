from classes.product import Product
from classes.order_line import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_available_stock(self, product: Product) -> int:
        available_stock = product.get_stock()
        for order_line in self.__order_lines:
            if order_line.get_product_id() == product.get_id():
                available_stock -= order_line.get_quantity()
        return available_stock

    def add_order_line(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        available_stock = self.get_available_stock(product)
        if quantity > available_stock:
            raise ValueError(f"Not enough stock. Only {available_stock} unit(s) available for this order.")

        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return total

    def display_information(self) -> None:
        print(f"\nOrder ID: {self.__order_id}")
        print("------------------------------------------------")
        for order_line in self.__order_lines:
            order_line.display_information()
        print("------------------------------------------------")
        print(f"Order Total: ${self.calculate_total():.2f}")
