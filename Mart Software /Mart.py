import time
import random

Stock = [
    [1, "Apple", 20, 40, "1 kg"],
    [2, "Milk", 10, 80, "1 ltr"],
    [3, "Water", 0, 10, "1 ltr"],
    [4, "Oil", 5, 60, "1 ltr"],
    [5, "Wheat Flour", 5, 45, "1 kg"],
    [6, "Salt", 10, 20, "500 gm"],
    [7, "Sugar", 15, 30, "1 kg"],
]


class Store:
    def __init__(self):
        self.all_orders = []
        self.current_cart = []

        while True:
            print("\n" + "=" * 35)
            print("Welcome to Gen-Z Mart")
            print("=" * 35)
            print(f"{' ' * 12}Choose Option")
            print("-" * 35)
            print("1. View Order History & Sales")
            print("2. Item Menu (Place Order)")
            print("3. Stock Report")
            print("4. Add Stock (Restock)") 
            print("0. Exit")
            choice = input("Please Select an Option: ")

            if choice == "0":
                print("Thank you for visiting Gen-Z Mart!")
                break
            elif choice == "1":
                self.order_history_list()
            elif choice == "2":
                self.menu()
            elif choice == "3":
                self.report()
            elif choice == "4":
                self.add_stock()
            else:
                print("Please enter a valid Option")

    # Order History Display
    def order_history_list(self):
        if not self.all_orders:
            print("\nNo orders have been placed yet.")
            return

        print("\n" + "=" * 125)
        print(f"{' ' * 50}ALL ORDER LOGS & SALES HISTORY")
        print("-" * 125)
        ord_column = ['Idx', 'Order ID', 'Items Purchased', 'Total Price', 'UPI ID', 'Trans ID', 'Trans Date']
        print(
            f"{ord_column[0]:<5} {ord_column[1]:<12} {ord_column[2]:<30} {ord_column[3]:<12} {ord_column[4]:<15} {ord_column[5]:<12} {ord_column[6]}")
        print("-" * 125)

        grand_total = 0
        for index, order_info in enumerate(self.all_orders):
            grand_total += order_info['total']
            print(
                f"{index:<5} #{order_info['id']:<11} {order_info['items_box']:<30} ${order_info['total']:<11} {order_info['upi']:<15} {order_info['tid']:<12} {order_info['time']}")

        print("-" * 125)
        print(f"{'':<5} {'':<12} {'GRAND TOTAL STORE REVENUE =':<30} ${grand_total:<11}")
        print("=" * 125)

    def menu(self):
        print("\n" + "-" * 35)
        for s in Stock:
            print(f"{s[0]}. {s[1]} - ${s[3]} per {s[4]} (Stock: {s[2]})")
        print("-" * 35)
        self.order_item()

    def order_item(self):
        self.current_cart = []
        while True:
            try:
                items = int(input("Enter Item By Number ('0' to proceed to checkout): "))

                if items == 0:
                    break

                if items < 1 or items > len(Stock):
                    print("Item Not Available At This Moment")
                    continue

                data = Stock[items - 1]
                stock = int(data[2])

                if stock == 0:
                    print("Low Stock!, New Stock Add Soon.")
                else:
                    self.current_cart.append(items)
                    data[2] = data[2] - 1
                    print(f"Added {data[1]} to cart.")
            except ValueError:
                print("Please enter a valid Item Number")

        if self.current_cart:
            self.order_checkout()
        else:
            print("Cart is empty. No order placed.")

    def order_checkout(self):
        column = ['Item Name', 'Price', 'Quantity']
        current_total = 0
        items_names_list = []

        print("\n" + "=" * 35)
        print(f"{' ' * 12}Your Cart")
        print("-" * 35)
        print(f"{column[0]:<15} {column[1]:<10} {column[2]}")
        print("-" * 35)

        for i in self.current_cart:
            data = Stock[i - 1]
            current_total += data[3]
            items_names_list.append(data[1])
            print(f"{data[1]:<15} ${data[3]:<10} {data[4]}")

        print("-" * 35)
        print(f"{'':<15} {'Total =':<11} ${current_total}")
        print("=" * 35)

        payment = input("Please Select Payment Method (Cash / Online): ").capitalize()
        if payment == "Online":
            upi_id = input("Enter UPI ID: ")
            trans_id = int(input("Enter Transaction ID: "))
        else:
            upi_id = "Cash"
            trans_id = 0

        trans_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        rtxt = ''
        for i in range(3):
            txt = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            rtxt += txt
        ord_no = rtxt + str(random.randint(1000, 1000000))

        items_in_one_box = ", ".join(items_names_list)

        order_receipt = {
            'id': ord_no,
            'items_box': items_in_one_box,
            'total': current_total,
            'upi': upi_id,
            'tid': trans_id,
            'time': trans_time
        }
        self.all_orders.append(order_receipt)

        print(f"\nSuccess! Your Order ID is #{ord_no}.")

    # Add Stock / Restock Items
    def add_stock(self):
        print("\n" + "=" * 50)
        print(f"{' ' * 18}RESTOCK INVENTORY")
        print("-" * 50)
        for s in Stock:
            print(f"{s[0]}. {s[1]:<15} (Current Stock: {s[2]})")
        print("-" * 50)

        try:
            item_num = int(input("Enter Item Number to add stock (or 0 to cancel): "))
            if item_num == 0:
                print("Restocking canceled.")
                return

            if item_num < 1 or item_num > len(Stock):
                print("Invalid Item Number.")
                return

            qty_to_add = int(input(f"Enter quantity of {Stock[item_num - 1][1]} to add: "))
            if qty_to_add < 0:
                print("Quantity cannot be negative.")
                return

            Stock[item_num - 1][2] += qty_to_add
            print(f"\nSuccessfully added stock! New {Stock[item_num - 1][1]} stock: {Stock[item_num - 1][2]}")

        except ValueError:
            print("Please enter a valid numeric value.")

    def report(self):
        print("\n" + "=" * 50)
        print(f"{' ' * 16}Current Stock Report")
        print("-" * 50)
        print(f"{'ID':<5} {'Item Name':<18} {'Available Stock':<15} {'Price'}")
        print("-" * 50)
        for s in Stock:
            print(f"{s[0]:<5} {s[1]:<18} {s[2]:<15} ${s[3]} per {s[4]}")
        print("=" * 50)


# Run the system
Mart = Store()
