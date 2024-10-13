import os
import json


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def load_inventory(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}  


def save_inventory(inventory, file_path):
    sorted_inventory = dict(sorted(inventory.items()))  
    with open(file_path, 'w') as f:
        json.dump(sorted_inventory, f, indent=4)


def add_update_item(inventory, product_id, item_name, quantity):
    if product_id in inventory:
        inventory[product_id]['quantity'] += quantity  
    else:
        inventory[product_id] = {'name': item_name, 'quantity': quantity} 

def delete_item(inventory, product_id):
    if product_id in inventory:
        del inventory[product_id]
        print(f"Product ID {product_id} has been deleted.")
    else:
        print(f"Product ID {product_id} not found.")


def display_inventory(inventory):
    if inventory:
        print("\nCurrent Inventory (sorted by Product ID):")
        for product_id, details in sorted(inventory.items()):
            print(f"ID: {product_id}, Name: {details['name']}, Quantity: {details['quantity']}")
    else:
        print("\nInventory is empty.")

def main():
    folder_name = "grocery_inventory"
    file_name = "inventory.json"
    file_path = os.path.join(folder_name, file_name)
    
    
    create_folder(folder_name)
    
   
    inventory = load_inventory(file_path)
    
    while True:
        print("\n--- Grocery Inventory Menu ---")
        print("1. Add/Update product")
        print("2. View inventory")
        print("3. Delete product")
        print("4. Exit")
        
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            try:
                product_id = input("Enter the product ID: ").strip()
                item_name = input("Enter the product name: ").strip()
                quantity = int(input("Enter the quantity: "))
                add_update_item(inventory, product_id, item_name, quantity)
                save_inventory(inventory, file_path)
                print(f"Product ID {product_id} - {item_name} has been added/updated.")
            except ValueError:
                print("Please enter a valid quantity.")
        
        elif choice == '2':
            display_inventory(inventory)
        
        elif choice == '3':
            product_id = input("Enter the product ID to delete: ").strip()
            delete_item(inventory, product_id)
            save_inventory(inventory, file_path)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please select again.")

if __name__ == "__main__":
    main()
