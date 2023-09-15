import json
from prettytable import PrettyTable

# Function to load inventory from a JSON file
def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save inventory to a JSON file
def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

# Function to load sales records from a JSON file
def load_sales_records():
    try:
        with open("sales_records.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save sales records to a JSON file
def save_sales_records():
    with open("sales_records.json", "w") as file:
        json.dump(sales_records, file)

# Initialize snack inventory by loading from the JSON file
inventory = load_inventory()

# Initialize sales records by loading from the JSON file
sales_records = load_sales_records()

# Function to add a snack to the inventory
def add_snack():
    snack_id = input("Enter Snack ID: ")
    snack_name = input("Enter Snack Name: ")
    price = float(input("Enter Price: "))
    availability = input("Is the snack available? (yes/no): ").lower()
    
    snack = {
        "ID": snack_id,
        "Name": snack_name,
        "Price": price,
        "Availability": availability
    }
    
    inventory.append(snack)
    print(f"{snack_name} has been added to the inventory.")
    save_inventory()

# Function to remove a snack from the inventory
def remove_snack():
    snack_id = input("Enter Snack ID to remove: ")
    for snack in inventory:
        if snack["ID"] == snack_id:
            inventory.remove(snack)
            print(f"{snack['Name']} has been removed from the inventory.")
            save_inventory()
            return
    print("Snack not found in inventory.")

# Function to update the availability of a snack
def update_availability():
    snack_id = input("Enter Snack ID to update availability: ")
    availability = input("Is the snack available? (yes/no): ").lower()
    for snack in inventory:
        if snack["ID"] == snack_id:
            snack["Availability"] = availability
            print(f"Availability of {snack['Name']} has been updated.")
            save_inventory()
            return
    print("Snack not found in inventory.")

# Function to record a sale
def record_sale():
    snack_id = input("Enter Snack ID sold: ")
    for snack in inventory:
        if snack["ID"] == snack_id:
            if snack["Availability"] == "yes":
                snack["Availability"] = "no"
                print(f"{snack['Name']} has been sold.")
                save_inventory()
                # Record the sale in sales_records
                sale_record = {
                    "ID": snack_id,
                    "Name": snack["Name"],
                    "Price": snack["Price"]
                }
                sales_records.append(sale_record)
                save_sales_records()
                return
            else:
                print(f"{snack['Name']} is not available.")
                return
    print("Snack not found in inventory.")

# Function to display all items in a tabular format
def get_all_items():
    if not inventory:
        print("Inventory is empty.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Availability", "Price"]
        for snack in inventory:
            table.add_row([snack["ID"], snack["Name"], snack["Availability"], snack["Price"]])
        print(table)

# Function to display all sales records in a tabular format
def get_all_sales_records():
    if not sales_records:
        print("Sales records are empty.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price"]
        for sale_record in sales_records:
            table.add_row([sale_record["ID"], sale_record["Name"], sale_record["Price"]])
        print(table)

# Main loop for user interaction
while True:
    print("\nMumbai Munchies Canteen")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Availability")
    print("4. Record Sale")
    print("5. Get All Items in Inventory")
    print("6. Get All Sales Records")
    print("7. Exit")
    
    choice = input("Enter your choice: (1/2/3/4/5/6/7)")
    
    if choice == "1":
        add_snack()
    elif choice == "2":
        remove_snack()
    elif choice == "3":
        update_availability()
    elif choice == "4":
        record_sale()
    elif choice == "5":
        get_all_items()
    elif choice == "6":
        get_all_sales_records()
    elif choice == "7":
        print("Exiting the application. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
