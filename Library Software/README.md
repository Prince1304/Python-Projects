# 📚 Gen-Z Library Management System

Welcome to the **Gen-Z Library Management System**—a lightweight, interactive CLI terminal application designed to manage a library inventory, secure admin controls, and handle real-time book orders seamlessly.

---

## ✨ Features

* **🔒 Secured Admin Space**: Protects Inventory management (Adding/Removing books) using a secure loop with real-time attempt tracking and brute-force lockout delays.
* **➕ Seamless Book Entry**: Adds new unique books automatically complete with details like Price, Quantities, and registration time.
* **❌ Dynamic Inventory Updates**: Remove books instantly from your database.
* **🛒 Order Placement System**: Real-time checkout flow that dynamically reduces available inventory count and attaches interactive live transaction dates.
* **📊 Structured Tables**: Beautifully organized, aligned custom columns for reading catalog entries and past invoice orders cleanly.

---

## 🛠️ Project Setup & Installation

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/) installed on your local machine.

### Setup Instructions
1. Clone or save your project file as `library.py`.
2. Open your terminal or command prompt in that directory and run:

```bash
python library.py
```

### 🗝️ Admin Credentials
To access restricted management choices (1 or 2), use these built-in default settings:
   Admin Password: admin123
   Note: Entering the wrong password 3 times triggers an automated 60-second lockout timer for security purposes.

### 📁 System Data Structures
The system tracks library assets using an organized sequence list design:
AttributeStructure     TypeData        Contained
self.Books             List of Lists   [Book Name, Price, Quantity, Author, Logged Date]
self.Order             List of Lists   [Book Name, Price, Ordered Qnty, Author, Logged Date, Order Timestamp]

### ⚙️ Core Logic Implementations
   Stock Tracking: Substracts current values seamlessly using simple step modifiers book[2] -= 1 immediately when items are added to a customer bag.
   Safe Order Appending: Uses list copying strategies via .copy() routines to preserve main catalog arrays without corrupting operational timestamps inside previous           customer purchases.

### 🚀 How To Navigate The App
```
When you launch the script, you are greeted with a main menu selection workflow:

