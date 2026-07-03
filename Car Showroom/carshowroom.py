import csv
import os
import time
import pandas as pd


class Cars:
    def __init__(self):
        print("=" * 100)
        self.name = input("Enter your Good name: ")
        print("=" * 100)
        print(f"Welcome {self.name} to Gen-Z Car Showroom")
        while True:
            print("=" * 100)
            print(f"{'Gen-Z Car Showroom Menu':^100}")
            print("=" * 100)
            print("1. Add Cars")
            print("2. Remove Cars")
            print("3. Show Cars")
            print("4. Buy Cars")
            print("5. View Orders")
            print("0. Exit")
            print("=" * 100)
            choice = input(f"{self.name} Please Enter your choice: ")
            print("I Am Opening...")
            if choice == "1":
                self.addcars()
            elif choice == "2":
                self.removecar()
            elif choice == "3":
                self.showcars()
            elif choice == "4":
                self.buycar()
            elif choice == "5":
                self.vieworder()
            elif choice == "0":
                self.out()
                break
            else:
                print(f"{self.name} Please Enter a valid Choice!")
    
    def security(self):
        print("=" * 50)
        print("This Only For Authorise Use")
        print("=" * 50)
        attempt = 3
        while True:
            if attempt == 0:
                print("Warning! You not Entering.")
                print("Try After 1 Minute.")
                time.sleep(60)
                attempt+=3
            else:
                password = input(f"Enter Password ({attempt} try left): ")
                if password == "admin123":
                    print("Welcome Admin!")
                    print("=" * 50)
                    return
                else:
                    print("Please Enter a Valid Password")
                    attempt -= 1
                    
    def addcars(self):
        self.security()
        while True:
            cname = input("Enter your car's name: ")
            try:
                df = pd.read_csv("cars.csv")
                df.columns = df.columns.str.strip()
                match = df[
                    (df["Car Name"].astype(str).str.lower() == cname.lower())
                    & (df["Status"] == "For Sale")
                ]
                if not match.empty:
                    print(
                        f"{self.name}, a car named '{cname}' is already listed 'For Sale'! Choose a unique name."
                    )
                    continue
                else:
                    car_name = cname
                    break
            except FileNotFoundError:
                car_name = cname
                break

        car_company = input("Enter your car's company: ")

        while True:
            try:
                price = int(input("Enter your car's price: "))
                break
            except ValueError:
                print("Please enter a valid numeric value for price!")

        car_model = input("Enter your car's model: ")

        while True:
            try:
                my = int(input("Enter your car's model year: "))
                if my > 2020:
                    model_year = my
                    break
                print(
                    f"{self.name} Please enter only above '2020' Cars Models!"
                )
            except ValueError:
                print("Please enter a valid numeric year!")

        while True:
            try:
                rk = int(input("Enter your car's runing km: "))
                if rk < 45000:
                    runing_km = rk
                    break
                print(
                    f"{self.name} Please enter a Under '45000'km Runing Cars!"
                )
            except ValueError:
                print("Please enter a valid numeric kilometer value!")

        while True:
            cond = input("Enter your car's condition(Good/Excellent): ")
            if cond in ["Good", "Excellent"]:
                car_condition = cond
                break
            print(
                f"{self.name} Please enter 'Good' or 'Excellent' car conditions!"
            )

        new_car_data = {
            "Car Name": [car_name],
            "Company": [car_company],
            "Price": [price],
            "Model": [car_model],
            "Year": [model_year],
            "KM": [runing_km],
            "Condition": [car_condition],
            "Status": ["For Sale"],
        }
        new_df = pd.DataFrame(new_car_data)

        try:
            file_exists = os.path.exists("cars.csv")
            new_df.to_csv(
                "cars.csv", mode="a", index=False, header=not file_exists
            )
            print(f"🎉 {car_name} is Added Successfully!")
        except PermissionError:
            print(
                f"❌ Sorry! {self.name}, close your 'cars.csv' file in Excel and try again!"
            )

    def removecar(self):
        self.security()
        car_name = input("Enter your car's name: ")
        try:
            df = pd.read_csv("cars.csv")
            df.columns = df.columns.str.strip()
            df.loc[
                df["Car Name"].astype(str).str.lower() == car_name.lower(),
                "Status",
            ] = "Not For Sale"
            df.to_csv("cars.csv", index=False)
            print(f"{car_name} is Removed Successfully!")
        except FileNotFoundError:
            print("❌ No cars available in the system yet.")
        except PermissionError:
            print("❌ System files are locked. Close Excel and try again.")

    def showcars(self):
        try:
            budget = int(input(f"{self.name} Enter Your Budget: "))
        except ValueError:
            print(f"{self.name} Please enter a valid number for your budget!")
            return

        try:
            df = pd.read_csv("cars.csv")
            df.columns = df.columns.str.strip()
            matching_cars = df[
                (df["Price"] <= budget) & (df["Status"] == "For Sale")
            ]

            if matching_cars.empty:
                print(f"No Match Found!")
            else:
                print("\n--- Matching Cars in Your Budget ---")
                for _, row in matching_cars.iterrows():
                    print(
                        f"{row['Car Name']} - {row['Year']} Model only for ₹{row['Price']}."
                    )
                print(
                    f"\nTotal {len(matching_cars)} cars found in your budget!"
                )
        except FileNotFoundError:
            print("❌ No cars available in the system yet.")

    def buycar(self):
        car_name = input("Enter the car name you want to buy: ")
        try:
            df = pd.read_csv("cars.csv")
            df.columns = df.columns.str.strip()

            match = df[
                (df["Car Name"].astype(str).str.lower() == car_name.lower())
                & (df["Status"] == "For Sale")
            ]

            if match.empty:
                print(f"❌ {self.name}, that car is not available for sale!")
                return

            idx = match.index[0]
            car_row = match.iloc[0]

            df.at[idx, "Status"] = "Sold"
            df.to_csv("cars.csv", index=False)

            order_data = {
                "Buyer": [self.name],
                "Car Name": [car_row["Car Name"]],
                "Company": [car_row["Company Name"]],
                "Price": [car_row["Price"]],
                "Model": [car_row["Model"]],
            }
            order_df = pd.DataFrame(order_data)

            order_file_exists = os.path.exists("orders.csv")
            order_df.to_csv(
                "orders.csv",
                mode="a",
                index=False,
                header=not order_file_exists,
            )
            print(f"🎉 Success! You have purchased the {car_row['Car Name']}!")

        except FileNotFoundError:
            print("❌ No cars available in the system yet.")
        except PermissionError:
            print("❌ System files are locked. Close Excel and try again.")

    def vieworder(self):
        try:
            df = pd.read_csv("orders.csv")
            df.columns = df.columns.str.strip()

            buyer_column = df["Buyer"].astype(str)
            my_orders = df[buyer_column.str.lower() == self.name.lower()]

            if my_orders.empty:
                print(f"ℹ️ {self.name}, you haven't bought any cars yet!")
            else:
                print(f"\n--- Order History for {self.name} ---")
                for _, row in my_orders.iterrows():
                    print(
                        f"Car: {row['Car Name']} | Company: {row['Company']} | Price: ₹{row['Price']} | Model: {row['Model']}"
                    )
                print(f"Total cars purchased: {len(my_orders)}")

        except FileNotFoundError:
            print("ℹ️ No orders have been placed in the system yet.")

    def out(self):
        print("=" * 100)
        print("I Hope you Enjoy with our Cars!")
        print("=" * 100)


cars = Cars()
