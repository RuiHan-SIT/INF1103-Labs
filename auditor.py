inventory = 0
failed_attempts = 0
stock = input("Enter stock quantity or 'quit' to exit: ")

while stock != "quit":
    if (stock.startswith("-") and stock[1:].isdigit()):
        failed_attempts += 1
        stock = input("Please enter a positive number or 'quit' to exit: ")
        continue
    elif not stock.isdigit():
        failed_attempts += 1
        stock = input("Please enter a valid number or 'quit' to exit: ")
        continue
    elif (inventory + int(stock) > 500):
        print("Inventory limit exceeded. Maximum capacity is 500 units.")
        failed_attempts += 1
        break
    else:
        inventory += int(stock)
        stock = input("Enter stock quantity or 'quit' to exit: ")
        continue

print("Inventory: ", inventory)
print("Number of failed attempts: ", failed_attempts)