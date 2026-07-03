import csv
import time
import pandas as pd

class Cars:
    name = ""
    def __init__(self):
        print("=" * 100)
        name = input("Enter your Good name: ")
        print("=" * 100)
        print(f"Welcome {name} to Gen-Z Car Showroom")
        while True:
            print("=" * 100)
            print(f"{'Gen-Z Car Showroom Menu':^100}")
            print("=" * 100)
            print("1. Add Cars")
            print("2. Remove Cars")
            print("3. Show Cars")
            print("0. Exit")
            print("="*100)
            choice = input(f"{name} Please Enter your choice: ")
            print("I Am Opening...")
            # time.sleep(3)
            if choice == "1":
                self.addcars()
            elif choice == "2":
                self.removecar()
            elif choice == "3":
                self.showcars()
            elif choice == "0":
                self.out()
            else:
                print(f"{name} Please Enter a valid Choice!")

    def addcars(self):
        try:
            car_name = input("Enter your car's name: ")
            car_company = input("Enter your car's company: ")
            price = input("Enter your car's price: ")
            car_model = input("Enter your car's model: ")
            while True:
                model_year = ''
                my = int(input("Enter your car's model year: "))
                if my > 2020:
                    my = model_year
                    break
                else:
                    print(f"{self.name} Please enter a only above '2020' Cars Models!")
            while True:
                runing_km = ''
                rk = int(input("Enter your car's runing km: "))
                if rk < 45000:
                    rk = runing_km
                    break
                else:
                    print(f"{self.name} Please enter a Under '45000'km Runing Cars!")
            while True:
                car_condition = ''
                cond = input("Enter your car's condition(Good/Excellent): ")
                if cond == 'Good' or cond == 'Excellent':
                    car_condition = cond
                    break
                else:
                    print(f"{self.name} Please enter a 'Good' or 'Excellent' car conditions! ")
            with open('cars.csv', 'a',newline='') as csvfile:
                writer = csv.writer(csvfile)
                status = 'For Sale'
                writer.writerow([car_name, car_company, price, car_model, model_year,runing_km, car_condition, status])
                print(f"{car_name} is Added Successfully!")
        except FileNotFoundError:
            print(f"Sorry! {self.name}, File Not Open Try Again")
