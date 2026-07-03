# 🚗 Gen-Z Car Showroom Management System

Welcome to the **Gen-Z Car Showroom Management System**—a robust, interactive command-line interface (CLI) application built using Python and `pandas`. It acts as a digital dealership allowing administrators to register vehicles and users to browse, filter by budget, and buy cars with real-time persistent data tracking.

---

## ✨ Features

* **📦 CSV Data Persistence**: All listings and orders are permanently saved inside local database files (`cars.csv` and `orders.csv`).
* **🔒 Authorized Admin Control**: Protects core dealership actions (Listing and Removing cars) using a secure administrative password gate featuring a built-in brute-force cooldown delay.
* **🛡️ Smart Data Validation**: Ensures inventory quality control by only accepting pristine models (Model year must be **above 2020**, mileage **under 45,000 km**, and condition set to **Good** or **Excellent**).
* **💰 Budget-Based Search**: Customers can instantly filter the entire showroom collection to only display active listings matching their specific financial budget.
* **🛒 Transaction Flow**: Automates checkouts by switching a car's catalog state to `"Sold"` and logging a custom sales receipt directly into the buyer's order history.
* **📂 Collision Prevention**: Features custom exceptions to notify you if you accidentally leave a database file open in Microsoft Excel or another program while the app tries to update.

---

## 🔑 Administrative Access
### Options 1 and 2 are restricted to dealership personnel.
Default Password: admin123
Note: Failing the security gate 3 times triggers an automated 60-second system lock for unauthorized login prevention.

---

## 🛠️ System Requirements & Installation

### 1. Prerequisites
Make sure you have [Python 3.x](https://www.python.org/) installed along with the `pandas` data-science framework.

### 2. Install Dependencies
Open your terminal or command prompt and install the required library package:
```bash
pip install pandas
```
### 3. Run Software
```
python Carshowroom.py
```

## 🚀 How to Navigate the Dealership
### When you open the system, you will be prompted to enter your name before the interactive main dashboard loads up:
```
====================================================================================================
                                      Gen-Z Car Showroom Menu                                       
====================================================================================================
1. Add Cars
2. Remove Cars
3. Show Cars
4. Buy Cars
5. View Orders
0. Exit
====================================================================================================
```

## 🔒 2. Choice 1: Add Cars (Admin Gate & Validation)
### Selecting option 1 triggers the security check. Once authorized, it enforces your strict validation parameters (Year > 2020, KM < 45000, Condition: Good/Excellent).
```
Prince Please Enter your choice: 1
I Am Opening...
==================================================
This Only For Authorise Use
==================================================
Enter Password (3 try left): admin123
Welcome Admin!
==================================================
Enter your car's name: Civic
Enter your car's company: Honda
Enter your car's price: 2200000
Enter your car's model: ZX Sedan

Enter your car's model year: 2018
Prince Please enter only above '2020' Cars Models!
Enter your car's model year: 2024

Enter your car's runing km: 50000
Prince Please enter a Under '45000'km Runing Cars!
Enter your car's runing km: 12000

Enter your car's condition(Good/Excellent): Old
Prince Please enter 'Good' or 'Excellent' car conditions!
Enter your car's condition(Good/Excellent): Excellent
🎉 Civic is Added Successfully!
```

## 💰 3. Choice 3: Show Cars (Filtering by Budget)
### This option prompts the user for a financial ceiling and filters the database layout to only display items marked "For Sale" matching that constraint.
```
Prince Please Enter your choice: 3
I Am Opening...
Prince Enter Your Budget: 2500000

--- Matching Cars in Your Budget ---
Civic - 2024 Model only for ₹2200000.

Total 1 cars found in your budget!
```

## 🛒 4. Choice 4: Buy Cars (Inventory State Update)
### When a user buys a car, the status in cars.csv shifts to "Sold", and an entry is generated inside orders.csv.
```
Prince Please Enter your choice: 4
I Am Opening...
Enter the car name you want to buy: Civic
🎉 Success! You have purchased the Civic!
```

## 🧾 5. Choice 5: View Orders (Transaction Receipts)
### This reads your purchase records directly from orders.csv matching your logged user profile token.
```
Prince Please Enter your choice: 5
I Am Opening...

--- Order History for Prince ---
Car: Civic | Company: Honda | Price: ₹2200000 | Model: ZX Sedan
Total cars purchased: 1
```

## ❌ 6. Choice 0: Exit
### Terminating the run updates the execution terminal cycle and prints the final exit sign-off block.
```
Prince Please Enter your choice: 0
I Am Opening...
====================================================================================================
I Hope you Enjoy with our Cars!
====================================================================================================

Process finished with exit code 0
```
