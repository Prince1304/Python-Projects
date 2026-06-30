# 🛒 Gen-Z Mart - Inventory & Point of Sale (POS) System

Gen-Z Mart is a console-based Retail Management and Point of Sale (POS) application built using Python. The application enables terminal-based storefront operations, including dynamic inventory tracking, multi-item cart checkouts, secure mock transaction processing (Cash/UPI), real-time stock reporting, and back-office restocking operations.

## ✨ Features

* **Interactive Menu System:** A looping control interface navigating between customer ordering, management logs, and inventory controls.
* **Consolidated Order History ("One-Box" Tracking):** Bundles all items checked out in a single session into a unified transaction entry, calculating a rolling **Grand Store Revenue** across all sessions.
* **Automated Metadata Generation:** Integrates Python's built-in `time` module for precise timestamping and the `random` module to generate distinct, alphanumeric Order IDs (e.g., `#aKz84923`).
* **Real-time Stock Management:** Automatically deducts stock upon purchase validation, alerts operators of out-of-stock items, and includes an administrative **Restock Inventory** dashboard.
* **Defensive Design Architecture:** Built-in `try-except` blocks to handle out-of-bounds indices and malicious alphanumeric entries, ensuring continuous application uptime.

---

## 🛠️ Data Structure Schema

The core database operates on a structured multi-dimensional array (nested list matrix) tracking item attributes:

| Column Index | Field Attribute | Data Type | Example Data |
| :--- | :--- | :--- | :--- |
| `[0]` | Item ID | `int` | `1` |
| `[1]` | Item Name | `str` | `"Apple"` |
| `[2]` | Stock Count | `int` | `20` |
| `[3]` | Price (Unit) | `int` | `40` |
| `[4]` | Metrics/Scale | `str` | `"1 kg"` |

---

## 🚀 Getting Started

### Prerequisites
To execute the application, ensure you have **Python 3.x** installed on your system. No external third-party dependencies or libraries are required.

### Installation & Execution
1. Clone or download the script file into your project directory (e.g., `Mart.py`).
2. Open your terminal or command prompt and navigate to the directory:
   ```bash
   cd "path/to/your/Python Projects/Mart Software"

### Run the application script
python Mart.py

## 💻 Application Workflow Example

### Main Dashboard Interface

```
===== Welcome to Gen-Z Mart =====
      Choose Option
---------------------------------
1. View Order History & Sales
2. Item Menu (Place Order)
3. Stock Report
4. Add Stock (Restock)
5. Exit
---------------------------------
Please Select an Option:
```
### Order Log Receipt View
```
=============================================================================================================================
                                                 ALL ORDER LOGS & SALES HISTORY
-----------------------------------------------------------------------------------------------------------------------------
Idx   Order ID     Items Purchased                Total Price  UPI ID          Trans ID     Trans Date
-----------------------------------------------------------------------------------------------------------------------------
0     #xKd83421    Apple, Milk, Oil               $180         merchant@upi    98274392     2026-06-30 15:02:11
1     #LpQ19482    Water, Salt                    $30          Cash            0            2026-06-30 15:05:43
-----------------------------------------------------------------------------------------------------------------------------
                                                 GRAND TOTAL STORE REVENUE =    $210
=============================================================================================================================
```
### Add Stock View (Restock Inventory)
```
==================================================
                RESTOCK INVENTORY
--------------------------------------------------
1. Apple           (Current Stock: 20)
2. Milk            (Current Stock: 10)
3. Water           (Current Stock: 0)
4. Oil             (Current Stock: 5)
5. Wheat Flour     (Current Stock: 5)
6. Salt            (Current Stock: 10)
7. Sugar           (Current Stock: 15)
--------------------------------------------------
Enter Item Number to add stock (or 0 to cancel): 3
Enter quantity of Water to add: 50

Successfully added stock! New Water stock: 50
```
