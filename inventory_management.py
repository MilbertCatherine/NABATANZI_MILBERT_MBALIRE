# Inventory : dictionary: item -> quantity
inventory = {
    "Rice": 50,
    "Beans": 30,
    "Sugar": 20
}

while True:
    print("\nInventory Menu")
    print("1. Display Inventory")
    print("2. Update Stock")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity} units")

    elif choice == "2":
        item = input("Enter item name: ").capitalize()
        if item in inventory:
            change = int(input(f"Enter quantity to add/remove (e.g., 10 or -5): "))
            inventory[item] += change
            print(f"{item} updated. New quantity: {inventory[item]}")
        else:
            add = input(f"{item} not found. Add it to inventory? (y/n): ").lower()
            if add == "y":
                quantity = int(input("Enter starting quantity: "))
                inventory[item] = quantity
                print(f"{item} added with {quantity} units.")

    elif choice == "3":
        print("Exiting Inventory Manager...")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
