from classes.product import Product
from classes.order_line import OrderLine

class Order:
    def __init__(self, order_id: str):
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int):
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return total