menu={"burger":130,"pizza":299,"coffee":149,"salad":50}
print("""
burger    :    130
pizza      :     299
coffee    :     149
salad      :      50
""")
print("Welcome to Bytecore restaurant !!!")
total=0
item1=input("order item above menu list:-\n")
if item1 in menu:
    total+=menu[item1]
    print(f"your item {item1} has been added in your order!")
else:
    print("not available {item1} this item")
another=input("Do you want to another item,(yes/no)")

if another=="yes":
    item2=input("Select  item for menu")
    if item2 in menu:
        total+=menu[item2]
        print(f"your item {item2} has been added")
    else:
        print("not available {item2} for this item")
print("total amount:-",total)
    



