import json

def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    
    for item in inventory:
        print(f'ID: {item["id"]} | Name: {item["name"]} | Price: ${item["price"]:.2f} | Stock: {item["stock"]}')
    
    print("------------------------------------------------")

def add_product(inventory):
    print("Add New Product")

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")

    while True:
        price = input("Price($): ")

        try:
            price = float(price)

            if price >= 0:
                break
            else:
                print("Please enter a positive price.")

        except ValueError:
            print("Please enter a valid price.")

    while True:
        stock = input("Stock Quantity: ")

        if stock.isdigit():
            stock = int(stock)
            break
        else:
            print("Please enter a valid stock quantity.")

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("\nProduct added successfully!")

def update_stock(inventory):
    print("Update Stock")

    product_id = input("Enter Product ID: ").upper()

    for item in inventory:
        if item["id"] == product_id:
            print("\nProduct Found:")
            print(f'Name: {item["name"]}')
            print(f'Current Stock: {item["stock"]}\n')

            while True:
                new_stock = input("New Stock Quantity: ")

                if new_stock.isdigit():
                    new_stock = int(new_stock)
                    break
                else:
                    print("Please enter a valid stock quantity.")

            item["stock"] = new_stock
            print("\nStock updated successfully!")
            return

    print("\nProduct not found.")

def search_product(inventory):
    print("Search Product")

    product_id = input("Enter Product ID: ").upper()
    for item in inventory:
        if item["id"] == product_id:
            print("\nProduct Found:")
            print("------------------------------------------------")
            print(f'ID: {item["id"]}')
            print(f'Name: {item["name"]}')
            print(f'Price: ${item["price"]:.2f}')
            print(f'Stock: {item["stock"]}')
            print("------------------------------------------------")
            return

    print("\nProduct not found.")

def load_inventory():
    try: 
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

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
        display_all(inventory)
    elif choice == 2:
        add_product(inventory)
    elif choice == 3:
        update_stock(inventory)
    elif choice == 4:
        search_product(inventory)
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