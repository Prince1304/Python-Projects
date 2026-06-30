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
