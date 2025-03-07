#THE MENU OF THE CAFE :
# Tea - Rs 70
# Coffee - Rs 80
# Burger - Rs 150
# Pizza - Rs 200
# Pasta - Rs 180 

menu = {
    'Tea': 70,
    'Coffee' : 80,
    'Burger' : 150,
    'Pizza' : 200,
    'Pasta' : 180
}

print("Welcome to Restaurant")
print("Tea: 70\n Coffee: 80\n Burger: 150\n Pizza: 200\n Pasta: 180")

total_order = 0

item_1 = input("Enter the name of item you want to order :")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been added in your cart")
else:
    print(f"Order item {item_1} is not available !")

another_order = input ("Do you want to add more item in your cart ?(yes/no) :")
if another_order == "yes":
    item_2 = input ("Enter the name of second item :")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Your item {item_2} has been added in your cart")
    else:
        print(f"Order item {item_2} is not available !")
        
print(f"The total amount of the item = Rs.{total_order}")
    