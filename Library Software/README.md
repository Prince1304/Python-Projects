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
   Stock Tracking: Substracts current values seamlessly using simple step modifiers book[2] -= 1 immediately when items are
   added to a customer bag.
   Safe Order Appending: Uses list copying strategies via .copy() routines to preserve main catalog arrays without
   corrupting operational timestamps inside previous customer purchases.

## 🚀 How To Navigate The App
## When you launch the script, you are greeted with a main menu selection workflow:
```
==================================================
Welcome to Gen-Z Library
==================================================
1. Add Book
2. Remove Book
3. Show Books
4. Order Books
5. View Orders
0. Exit
--------------------------------------------------
Enter your choice:
```

## Choice 1: Add Book & Security Prompt
### Scenario A: Successful Password
```
Enter your choice: 1
==================================================
This Only For Authorise Use
==================================================
Enter Password (3 try left): admin123
Welcome Admin!
==================================================
Enter Book Name: Python Pro
Enter Book Price: 1200
Enter Book Quantity: 5
Enter Book Author: Guido Van
--------------------------------------------------
Python Pro has been added to the Books List.
--------------------------------------------------
```

### Scenario B: Wrong Password & Security Lockout
If an unauthorized person attempts to enter, it locks them down for 60 seconds after 3 missed attempts.
```
Enter your choice: 1
==================================================
This Only For Authorise Use
==================================================
Enter Password (3 try left): wrong1
Please Enter a Valid Password
Enter Password (2 try left): wrong2
Please Enter a Valid Password
Enter Password (1 try left): wrong3
Please Enter a Valid Password
Warning! You not Entering.
Try After 1 Minute.
...(System sleeps for 60 seconds)...
Enter Password (3 try left):
```

## Choice 3: Show Books (Initial Catalog)
### If you view the catalog immediately, it shows the pre-loaded hardcoded book "Ai + Me".
```
Enter your choice: 3
====================================================================================================
                                            My Book List                                            
====================================================================================================
Index     Book Name       Book Price      Book Quantity   Book Author     Book Date      
----------------------------------------------------------------------------------------------------
1         Ai + Me         9000            1               kp patel        Wed, 01 Jul 2026
====================================================================================================
1. Add Book
2. Remove Book
3. Show Books
4. Order Books
5. View Orders
0. Exit
--------------------------------------------------
Enter your choice:
```

## Choice 4:🛒 Order Books (Stock Reduction)
### When you place an order, it displays the ordering menu. Let's order the book "Ai + Me".
```
Enter your choice: 4
=============================================
                My Book List                 
=============================================
Index     Book Name       Price       Qnty     
---------------------------------------------
1         Ai + Me         9000            1              
2         Python Pro      1200            5              
=============================================
Enter Order Book Name (Press 'o' for Order): Ai + Me
Enter Order Book Name (Press 'o' for Order): o
```

## Choice 5:📄 View Orders
### This outputs the exact receipt details of what was successfully ordered, complete with the second-by-second precise checkout timestamp.
```
Enter your choice: 5
==============================================================================================================
                                              My Order Book List                                              
==============================================================================================================
Index Book Name  Price      Qnty       Author          Publish Date         Order Date          
--------------------------------------------------------------------------------------------------------------
1     Ai + Me    9000       1          kp patel        Wed, 01 Jul 2026     Wed, 01 Jul 2026 14:59:11
==============================================================================================================
1. Add Book
2. Remove Book
3. Show Books
4. Order Books
5. View Orders
0. Exit
--------------------------------------------------
Enter your choice:
```

