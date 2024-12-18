menu = {"burger": 130, "pizza": 299, "coffee": 149, "salad": 50}

# Print the menu
print("""
burger    :    130
pizza     :    299
coffee    :    149
salad     :    50
""")

print("Welcome to Bytecore restaurant !!!")
total = 0

# Order the first item
item1 = input("Order item from the above menu list:\n")
if item1 in menu:
    total += menu[item1]
    print(f"Your item {item1} has been added to your order!")
else:
    print(f"Not available {item1} in the menu.")

# Ask if the user wants to add another item
another = input("Do you want another item? (yes/no): ").lower()

while another == "yes":
    item2 = input("Select an item from the menu: ")
    if item2 in menu:
        total += menu[item2]
        print(f"Your item {item2} has been added to your order!")
    else:
        print(f"Not available {item2} in the menu.")
    another = input("Do you want another item? (yes/no): ").lower()

print(f"Total amount: {total}")

