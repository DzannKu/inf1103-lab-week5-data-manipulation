import json
import os

inventory = [
    {
        "ID" : "P001",
        "Name" : "Laptop",
        "Price" : "1200.00",
        "Stock" : "15",
    },

    {
        "ID" : "P002",
        "Name" : "Mouse",
        "Price" : "25.50",
        "Stock" : "40",
    },

    {
        "ID" : "P003",
        "Name" : "Keyboard",
        "Price" : "45.00",
        "Stock" : "25",
    }

]


#functions
def load_inventory(): #read inventory.json
    try:
        with open("inventory.json", "r") as file:
            print("inventory.json found.")
            inventory = json.load(file)
            print("Inventory loaded successfully.")
            return inventory

    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")
        return []

def save_inventory(inventory): #write inventory.json
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
        print("Saving inventory...")
    
def add_product():
    print("Add New Product")
    new_id = input("Product ID: ")
    new_name = input("Product Name: ")
    new_price = input("Price: ")
    new_stock = input("Stock Quantity: ")
    inventory.append({"ID": new_id, "Name": new_name, "Price": new_price, "Stock": new_stock})
    print("")
    print(f"Product added successfully!")

def update_stock():
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product["ID"] == product_id:
            print("Product found!")
            print("")
            print("Name: ", product["Name"])
            print("Current Stock: ", product["Stock"])
            print("")
            new_stock = input("Enter New Stock Quantity: ")
            product["Stock"] = new_stock
            print("")
            print("Stock updated successfully!")
            return
    print("Product not found.")

def search_product():
    print("Search Product")
    search_id = input("Enter Product ID: ")
    found_products = []
    for product in inventory:
        if product["ID"] == search_id:
            found_products.append(product)
    if found_products:
        print("Product found:")
        print("")
        for product in found_products:
            print("------------------------------")
            print(f"ID: {product['ID']}")
            print(f"Name: {product['Name']}")
            print(f"Price: ${product['Price']}")
            print(f"Stock: {product['Stock']}")
            print("------------------------------")
    else:
        print("")
        print("Product not found.")

def exit_program():
    print("Saving inventory before exiting...")
    save_inventory(inventory)
    print("Inventory saved successfully.")
    print("")
    print("Thank you for using the Inventory Management System")
    print("Program terminated.")
    exit()

def display_all():
    inventory_Length = len(inventory)
    print("Current Inventory")
    print ("------------------------------")
    for i in range(inventory_Length):
        print(f"ID: {inventory[i]['ID']} | Name: {inventory[i]['Name']} | Price: ${inventory[i]['Price']} | Stock: {inventory[i]['Stock']}")
    print ("------------------------------")
def user_menu():
    print("------------ MENU ------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------------")
    while True:
        print("")
        user_option = input("Enter option: ")
        print("")
        if user_option == "1":
            display_all()
            continue
        elif user_option == "2":
            add_product()
            continue
        elif user_option == "3":
            update_stock()
            continue
        elif user_option == "4":
            search_product()
            continue
        elif user_option == "5":
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
            continue
        elif user_option == "6":
            exit_program()
            break
user_menu()
