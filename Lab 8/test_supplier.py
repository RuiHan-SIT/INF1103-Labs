from classes.supplier import Supplier
from classes.physical_product import PhysicalProduct
from classes.order import Order

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")
product = PhysicalProduct("P001", "Laptop", 1200, 10, 2.5, supplier)

order1 = Order("O001")
order2 = Order("O002")

order1.add_order_line(product, 2)
order2.add_order_line(product, 3)

print(f"Order 1 Total: ${order1.calculate_total():.2f}")
print(f"Order 2 Total: ${order2.calculate_total():.2f}")