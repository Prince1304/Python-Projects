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
