import json
from classes.inventory import Inventory
from classes.physical_product import PhysicalProduct
from classes.digital_product import DigitalProduct
from classes.supplier import Supplier
from classes.order import Order

def add_product_menu(inventory):
    print("Add New Product\n")

    print("Select Product Type:")
    print("1. Physical Product")
    print("2. Digital Product\n")

    while True:
        option = input("Enter option: ")

        try:
            option = int(option)

            if option == 1 or option == 2:
                break
            else:
                print("Please enter only option '1' or '2'.")

        except ValueError:
            print("Please enter a valid option.")

    while True:
        product_id = input("\nProduct ID: ").upper()
        result = inventory.search_product(product_id)

        if result is not None:
            print("Error: Product ID already exists. Please enter a different ID.")
        else:
            break    

    product_name = input("Product Name: ")

    while True:
        price = input("Price($): ")

        try:
            price = float(price)

            if price >= 0:
                break
            else:
                print("Please enter a non-negative price.")

        except ValueError:
            print("Please enter a valid price.")
    
    while True:
        stock = input("Stock Quantity: ")

        try:
            stock = int(stock)

            if stock >= 0:
                break
            else:
                print("Please enter a valid stock quantity.")

        except ValueError:
            print("Please enter a valid stock quantity.")

    if option == 1:
        while True:
            weight = input("Weight: ")

            try:
                weight = float(weight)
    
                if weight >= 0:
                    break
                else:
                    print("Please enter a valid weight.")
    
            except ValueError:
                print("Please enter a valid weight.")

    
    elif option == 2:
        while True:
            download_size = input("Download Size: ")

            try:
                download_size = int(download_size)
    
                if download_size >= 0:
                    break
                else:
                    print("Please enter a valid download size.")
    
            except ValueError:
                print("Please enter a valid download size.")

    
    print("\nSupplier Details")
    supplier_id = input("Supplier ID: ").strip().upper()
    supplier_name = input("Supplier Name: ").strip()
    contact_email = input("Supplier Email: ").strip()
    supplier = Supplier(supplier_id, supplier_name, contact_email)

    if option == 1:
        product = PhysicalProduct(product_id, product_name, price, stock, weight, supplier)
    else:
        product = DigitalProduct(product_id, product_name, price, stock, download_size, supplier)

    inventory.add_product(product)
    print("\nProduct added successfully!")

def update_stock_menu(inventory):
    print("Update Stock")

    product_id = input("Enter Product ID: ").upper()

    result = inventory.search_product(product_id)

    if result is not None:
        print("\nProduct Found:")
        print(f"Name: {result.get_name()}")
        print(f"Current Stock: {result.get_stock()}")
        while True:
            new_stock = input("\nNew Stock Quantity: ")
    
            if new_stock.isdigit():
                new_stock = int(new_stock)
                result.update_stock(new_stock)
                print("\nStock updated successfully!")
                break
            else:
                print("Please enter a valid stock quantity.")
    else:
        print("Product not found.")

def search_product_menu(inventory):
    print("Search Product")

    product_id = input("Enter Product ID: ").upper()
    result = inventory.search_product(product_id)
    if result is not None:
        print("\nProduct Found:")
        result.display_detailed_information()
        result.display_supplier_information()
    else:
        print("\nProduct not found.")

def create_order_menu(inventory: Inventory) -> None:
    if not inventory.get_products():
        print("No products available. Add a product first.")
        return

    order_id = input("Enter Order ID: ").strip().upper()
    while not order_id:
        order_id = input("Order ID is required. Enter Order ID: ").strip().upper()

    order = Order(order_id)
    line_count = 0
    inventory.display_all()

    while True:
        product_id = input("\nProduct ID to order (0 to finish): ").strip().upper()
        if product_id == "0":
            break

        product = inventory.search_product(product_id)
        if product is None:
            print("Product not found. Please try again.")
            continue

        available_stock = order.get_available_stock(product)
        if available_stock <= 0:
            print("No units remain available for this product in this order.")
            continue
        print(f"Available for this order: {available_stock}")

        while True:
            try:
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Please enter a whole number.")
                continue

            try:
                # Order validates stock and creates the OrderLine internally.
                order.add_order_line(product, quantity)
                break
            except ValueError as error:
                print(error)

        line_count += 1
        print("Order line added.")

    if line_count == 0:
        print("No order lines added. Order cancelled.")
        return

    order.display_information()


def load_inventory():
    inventory = Inventory()
    try: 
        with open("inventory.json", "r") as file:
            data = json.load(file)

        # Older inventory files do not contain supplier details.
        unknown_supplier = Supplier("UNKNOWN", "Not recorded", "Not recorded")
        missing_suppliers = False

        for item in data:
            if "supplier" in item:
                supplier_data = item["supplier"]
                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )
            else:
                supplier = unknown_supplier
                missing_suppliers = True

            if item["type"] == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"], supplier)
            elif item["type"] == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"], supplier)

            inventory.add_product(product)
        
        print("inventory.json found.")
        print("Inventory loaded successfully.")
        if missing_suppliers:
            print("Some saved products have no supplier details; these are shown as Not recorded.")
        return inventory
    except FileNotFoundError:
        return inventory

def save_inventory(inventory):
    data = []
    products = inventory.get_products()
    for item in products:
        data.append(item.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

# =================================================
#                    MAIN MENU                    
# =================================================

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================\n")

    inventory = load_inventory()

    choice = ""

    while choice != 7:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Create Order")
        print("7. Exit")
        print("-------------------------------")

        choice = input("\nEnter option: ")
        print("")

        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid option. Please try again.")
            continue

        if choice == 1:
            inventory.display_all()
        elif choice == 2:
            add_product_menu(inventory)
        elif choice == 3:
            update_stock_menu(inventory)
        elif choice == 4:
            search_product_menu(inventory)
        elif choice == 5:
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif choice == 6:
            create_order_menu(inventory)
        elif choice == 7:
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.\n")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()