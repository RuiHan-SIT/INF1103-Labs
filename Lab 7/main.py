import json
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

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

        product = PhysicalProduct(product_id, product_name, price, stock, weight)
    
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

        product = DigitalProduct(product_id, product_name, price, stock, download_size)
    
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
    else:
        print("\nProduct not found.")

def load_inventory():
    inventory = Inventory()
    try: 
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"])
            elif item["type"] == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"])

            inventory.add_product(product)
        
        print("inventory.json found.")
        print("Inventory loaded successfully.")
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

    while choice != 6:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
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