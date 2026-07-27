# 💰 Expense Tracker

A command-line expense tracking application built with Python. Track your daily expenses, set monthly budgets, and analyze your spending patterns.

## ✨ Features

- **Set Monthly Budget** - Define your spending limit for the month
- **Add Expenses** - Record expenses with title, category, amount, and date
- **View All Expenses** - See all your expenses in a formatted table
- **Budget Summary** - Get an overview of your total spending vs budget
- **Spending Analysis** - Monthly breakdown with category-wise spending and visual bars
- **Edit / Delete Expenses** - Modify or remove existing expense records
- **Export to CSV** - Export your expense data to a timestamped CSV file
- **Persistent Storage** - All data automatically saved to `expenses.csv`
- **8 Predefined Categories** - Food, Transport, Shopping, Bills, Entertainment, Health, Education, Other

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prince1304/Python-Projects.git
   cd Python-Projects/Expense\ Tracker
   ```

2. **Run the application:**
   ```bash
   python MyBudget.py
   ```

No additional dependencies required. Works with Python 3.6+.

## 📖 Usage

1. Run `python MyBudget.py`
2. Enter your name when prompted
3. Use the menu to navigate options:
   - **Option 1** - Set your monthly budget
   - **Option 2** - Add a new expense (choose category, enter title and amount)
   - **Option 3** - View all recorded expenses
   - **Option 4** - View budget summary (total spent, remaining, category breakdown)
   - **Option 5** - Analyze spending (monthly breakdown, top expenses)
   - **Option 6** - Edit or delete an existing expense
   - **Option 7** - Export expenses to a CSV file
   - **Option 0** - Exit the application

### Example

```
========================================
         EXPENSE TRACKER
========================================
1. Set Monthly Budget
2. Add Expense
3. View All Expenses
4. View Summary
5. Analyze Spending
6. Edit / Delete Expense
7. Export Expenses to CSV
0. Exit
========================================
Enter Your Choice: 1
Enter Your Monthly Budget: $1000
```

## 📁 Project Structure

```
Expense Tracker/
├── MyBudget.py          # Main application file
├── test_MyBudget.py     # Unit tests
├── requirements.txt     # Dependencies (none required)
├── README.md            # This file
└── expenses.csv         # Auto-generated data file
```

## 🧪 Running Tests

```bash
python -m unittest test_MyBudget.py
```

## 🛠️ Built With

- Python 3 - Standard Library only
- CSV module for data persistence
- Datetime module for date tracking

## 👤 Author

**Prince Kyada**
- GitHub: [@Prince1304](https://github.com/Prince1304)

## 📝 License

This project is open source and available under the MIT License.

