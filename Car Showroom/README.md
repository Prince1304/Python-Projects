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

## 🛠️ System Requirements & Installation

### 1. Prerequisites
Make sure you have [Python 3.x](https://www.python.org/) installed along with the `pandas` data-science framework.

### 2. Install Dependencies
Open your terminal or command prompt and install the required library package:
```bash
pip install pandas
