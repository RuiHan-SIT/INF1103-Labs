inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]

def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    
    for item in inventory:
        print(f"ID: {item["id"]} | Name: {item["name"]} | Price: ${item["price"]:.2f} | Stock: {item["stock"]}")
    
    print("------------------------------------------------")

def add_product(inventory):
    print("Add New Product")

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")

    while True:
        price = input("Price: ")

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

    print("Product added successfully!")

def update_stock(inventory):
    print("Update Stock")

    product_id = input("Enter Product ID: ")

    for item in inventory:
        if item["id"] == product_id:
            print("\nProduct Found:")
            print(f"Name: {item["name"]}")
            print(f"Current Stock: {item["stock"]}\n")

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

    product_id = input("Enter Product ID: ")
    for item in inventory:
        if item["id"] == product_id:
            print("\nProduct Found:")
            print("------------------------------------------------")
            print(f"ID: {item["id"]}")
            print(f"Name: {item["name"]}")
            print(f"Price: ${item["price"]:.2f}")
            print(f"Stock: {item["stock"]}")
            print("------------------------------------------------")
            return

    print("Product not found.")