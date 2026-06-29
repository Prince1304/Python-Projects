menu = {
    "Cofee":80,"Chai":30,
    "Burger":40,"Pizza":50,
    "Pasta":70,"Milk":90,
}

print("Welcome to the Gen-Z Cafe")
name = input("Please enter your name: ").capitalize()
print(f"Hii,{name}\nPlease Order Something For Better Experience")

menu_index = 0
for key, value in menu.items():
    print(f"{key} is only for ${value}")
    menu_index += 1

print("-"*50)
print(f"{name} if You Complete Add Item Press O For Order!")
item = []
print("-"*50)
while True:
    order = input("Please enter your item: ").capitalize()
    if order == 'o' or order == 'O':
        break
    else:
        if order in menu.keys():
            item.append(order)
        else:
            print(f"Your Order Item :'{order}' Not Available at This Moment")

print("-"*50)
print(item)
print(f"Wow {name}, Such A Great Test!")
print("Your Order Is")

total = 0
for key, value in menu.items():
    Q = len(item)
    for ord_item in item:
        if ord_item == key:
            total+=value
            print(f"{ord_item}*{Q} :${value}")
            item.remove(ord_item)

print(f"Total Bill Is :${total}")
payment = input("Please Enter A Payment Mode (Cash/Online):").capitalize()
upi = ''
TID = ''
if payment == "Cash":
    pass
else:
    upi = input("Please Enter Your Upi ID: ")
    TID = input("Please Enter Your Transition ID: ")
print("Your Order Place!")
Table = ['A1','A2','A3','A4','A5']

print(f"Your Table Number Is '{Table[0]}' Please Be Seated!")
print("Thank For Trust on Gen-Z Cafe")

print("-"*50)
print("\n")
print("For Restrarant")
print(f"Order Arrive From Table No: {Table[0]}")
ind = 1
for i in item:
    print(f"{ind}:{i}")
    ind+=1
print(f"Total {ind-1} Item Order Found From Table No: {Table[0]}.")
print(f"Order Payment Mode: {payment}")
if payment == "Cash":
    print(f"Please Collects Cash ${total} on Table No: {Table[0]}")
else:
    print(f"Order Upi ID: {upi}")
    print(f"Order Transition ID: {TID}")
Table.pop(0)
