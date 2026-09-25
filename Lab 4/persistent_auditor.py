failed_attempts = 0
deliveries_processed = 0

def get_valid_input():
    failed_inputs = 0

    while True:
        stock = input("Enter stock quantity or 'quit' to exit: ")

        if stock == "quit":
            return "quit", failed_inputs

        elif stock.startswith("-") and stock[1:].isdigit():
            print("Please enter a positive number or 'quit' to exit.")
            failed_inputs += 1

        elif not stock.isdigit():
            print("Please enter a valid number or 'quit' to exit.")
            failed_inputs += 1

        else:
            return int(stock), failed_inputs

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = 0.1 * amount
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Inventory:", total_units)
    print("Number of failed attempts:", failed_attempts)

def load_inventory():
    file = open("inventory.txt", "a")
    file.close()

    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        return 0, []

    inventory = int(lines[1])
    history_lines = lines[4:]
    transaction_history = []

    for line in history_lines:
        transaction_history.append(int(line))

    return inventory, transaction_history

def save_inventory(inventory, transaction_history):
    with open("inventory.txt", "w") as file:
        file.write("Total Inventory (Units):\n")
        file.write(str(inventory) + "\n\n")
        file.write("Transaction History (Units):\n")

        for transaction in transaction_history:
            file.write(str(transaction) + "\n")

inventory, transaction_history = load_inventory()

print(f"Loaded Inventory: {inventory}")
print(f"Transaction History: {transaction_history}")

while True:
    delivery, input_failures = get_valid_input()

    failed_attempts += input_failures

    if delivery == "quit":
        save_inventory(inventory, transaction_history)
        break

    if inventory + delivery > 500:
        print("Inventory limit exceeded. Maximum capacity is 500 units.")
        failed_attempts += 1
        save_inventory(inventory, transaction_history)
        break

    inventory = process_delivery(inventory, delivery)
    deliveries_processed += 1
    transaction_history.append(delivery)
    
    tax = calculate_tax(delivery)
    print(f"Tax: ${tax}")

print("Total Deliveries Processed:", deliveries_processed)
generate_report(inventory, failed_attempts)