from classes.supplier import Supplier
from classes.product import Product
from classes.physical_product import PhysicalProduct
from classes.digital_product import DigitalProduct
from classes.inventory import Inventory
from classes.order import Order


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_association() -> None:
    supplier = Supplier("S001", "Lab Supplier", "supplier@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200.0, 5, 2.5, supplier)
    digital = DigitalProduct("D001", "Software", 150.0, 10, 500, supplier)
    del supplier
    physical.display_supplier_information()
    digital.display_supplier_information()
    print("PASS: both products still display their independent supplier.")


def test_aggregation() -> None:
    supplier = Supplier("S001", "Lab Supplier", "supplier@example.com")
    product = PhysicalProduct("P001", "Laptop", 1200.0, 5, 2.5, supplier)
    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(product)
    assert inventory_a.search_product("P001") is product
    inventory_a.remove_product("P001")
    assert inventory_a.search_product("P001") is None
    product.display_information()
    inventory_b.add_product(product)
    assert inventory_b.search_product("P001") is product
    print("PASS: the same product survives removal and transfers to Inventory B.")


def test_composition() -> None:
    supplier = Supplier("S001", "Lab Supplier", "supplier@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200.0, 5, 2.5, supplier)
    digital = DigitalProduct("D001", "Software", 150.0, 10, 500, supplier)
    order_a = Order("O001")
    order_b = Order("O002")
    order_a.add_order_line(physical, 2)
    order_b.add_order_line(physical, 3)
    assert order_a.calculate_total() == 2400.0
    assert order_b.calculate_total() == 3600.0
    print("Order A:", order_a.calculate_total())
    print("Order B:", order_b.calculate_total())
    # Add a second product to demonstrate a multi-line order total.
    order_a.add_order_line(digital, 1)
    order_a.display_information()
    assert order_a.calculate_total() == 2550.0
    assert order_b.calculate_total() == 3600.0
    del order_a
    assert physical.get_name() == "Laptop"
    assert digital.get_name() == "Software"
    print("PASS: orders create their own lines, calculate independent totals, and do not own the products.")


def test_lsp_and_polymorphism() -> None:
    supplier = Supplier("S001", "Lab Supplier", "supplier@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200.0, 5, 2.5, supplier)
    digital = DigitalProduct("D001", "Software", 150.0, 10, 500, supplier)
    inventory = Inventory()
    inventory.add_product(physical)
    inventory.add_product(digital)
    inventory.display_all()
    for product in inventory.get_products():
        show_product_details(product)
        product.update_stock(12)
        assert product.get_stock() == 12
        assert product.to_dict()["stock"] == 12
    assert physical.get_fulfilment_info() == "This product requires physical shipping."
    assert digital.get_fulfilment_info() == "This product is delivered digitally."
    print("PASS: both subclasses work through the Product contract and preserve stock-update behaviour.")


def test_supplier_serialisation() -> None:
    supplier = Supplier("S001", "Lab Supplier", "supplier@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200.0, 5, 2.5, supplier)
    digital = DigitalProduct("D001", "Software", 150.0, 10, 500, supplier)
    inventory = Inventory()
    inventory.add_product(physical)
    inventory.add_product(digital)
    for product in inventory.get_products():
        record = product.to_dict()
        assert record["supplier"] == supplier.to_dict()
    print("PASS: supplier details are included in both product types for JSON storage.")


def test_order_stock_limits() -> None:
    supplier = Supplier("S001", "Lab Supplier", "supplier@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier)
    digital = DigitalProduct("D001", "Software", 150.0, 10, 500, supplier)
    order = Order("STOCK01")
    for invalid_quantity in [20, 0, -1]:
        try:
            order.add_order_line(physical, invalid_quantity)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid order quantity was accepted")
        assert order.calculate_total() == 0

    order.add_order_line(physical, 10)
    assert order.get_available_stock(physical) == 5
    try:
        order.add_order_line(physical, 6)
    except ValueError:
        pass
    else:
        raise AssertionError("Repeated lines exceeded stock")
    assert order.calculate_total() == 12000.0
    order.add_order_line(physical, 5)
    assert order.get_available_stock(physical) == 0
    try:
        order.add_order_line(physical, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("An extra line was accepted after stock was exhausted")
    order.add_order_line(digital, 10)
    assert order.get_available_stock(digital) == 0
    try:
        order.add_order_line(digital, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("Digital product stock was exceeded")
    assert physical.get_stock() == 15
    assert digital.get_stock() == 10
    print("PASS: oversized, non-positive, repeated-line and out-of-stock quantities are rejected for both product types.")


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp_and_polymorphism()
    test_supplier_serialisation()
    test_order_stock_limits()
    print("\nALL LAB 8 CHECKS PASSED")
