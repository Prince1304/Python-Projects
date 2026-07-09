# ☕ Gen-Z Cafe - Automated Billing & Kitchen Routing System
 
Gen-Z Cafe is a console-based ordering, billing, and restaurant management script written in Python. It handles front-of-house customer interactions—including dynamic menu presentation, input validation, cart calculations, and payment tracking—while automatically routing order tickets to back-of-house kitchen displays with active table tracking.

## ✨ Features

* **Dynamic Customer Onboarding:** Greets users by name and presents an interactive menu dynamically parsed from a dictionary map.
* **Safe Order Accumulation:** Real-time checking against the menu keys prevents invalid orders, prompting immediate feedback for unavailable items.
* **Smart Billing Generation:** Cross-references the active cart array to parse items, automatically tallies item quantities, and updates total pricing values.
* **Dual Payment Processing Architecture:** Routes workflows depending on whether the user selects "Cash" or "Online" (requiring mock UPI and Transaction IDs).
* **Automated Table Allocation:** Dynamically queues available tables from an active array and safely pops them once assigned.
* **Kitchen Ticket Generation:** Automatically generates a formatted summary receipt detailing precise item indexes, quantities, payment details, and table locations for the restaurant staff.

---

## 🚀 Getting Started
### Prerequisites
Requires Python 3.x environment. No external packaging or libraries (pip) are necessary.

### Execution Instructions
1. Save the program script code as GenZ_Cafe.py.
2. Access your system terminal application.
3. Boot the console script runner:
   Save the program script code as Cafe.py.

Access your system terminal application.

Boot the console script runner:

## 💻 Application Workflow Example

### Front-of-House Customer Menu & Order

```text
Welcome to the Gen-Z Cafe
Please enter your name: Prince
Hii, Prince
Please Order Something For Better Experience
Cofee is only for $80
Chai is only for $30
Burger is only for $40
Pizza is only for $50
Pasta is only for $70
Milk is only for $90
--------------------------------------------------
Prince if You Complete Add Item Press O For Order!
--------------------------------------------------
Please enter your item: Burger
Please enter your item: Chai
Please enter your item: Pizza
Please enter your item: O
--------------------------------------------------
Wow Prince, Such A Great Test!
Your Order Is
Burger*3 :$40
Chai*2 :$30
Pizza*1 :$50
Total Bill Is :$120
Please Enter A Payment Mode (Cash/Online): Online
Please Enter Your Upi ID: prince@ybl
Please Enter Your Transition ID: TXN987654321
Your Order Place!
Your Table Number Is 'A1' Please Be Seated!
Thank For Trust on Gen-Z Cafe
--------------------------------------------------
```

### Back-of-House Kitchen Routing Ticket
```
For Restrarant
Order Arrive From Table No: A1
1: Burger
2: Chai
3: Pizza
Total 3 Item Order Found From Table No: A1.
Order Payment Mode: Online
Order Upi ID: prince@ybl
Order Transition ID: TXN987654321
```
