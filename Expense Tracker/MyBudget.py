import csv
import os
from datetime import datetime
from typing import Dict, List, Optional

CSV_FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Education", "Other"]


def load_expenses() -> List[Dict]:
    """Load expenses from CSV file. Returns empty list if file doesn't exist."""
    if not os.path.exists(CSV_FILE):
        return []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except (csv.Error, IOError):
        return []


def save_expenses(expenses: List[Dict]) -> None:
    """Save expenses list to CSV file."""
    with open(CSV_FILE, "w", newline="") as f:
        fieldnames = ["date", "category", "title", "amount"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


class Budget:
    def __init__(self):
        self.name = ""
        self.monthly_budget = 0.0
        self.expenses: List[Dict] = []
        self.get_or_create_user()

    def get_or_create_user(self) -> None:
        """Welcome the user and load existing data."""
        self.name = input("Please Enter Your Good Name: ").strip() or "User"
        self.expenses = load_expenses()
        print(f"\nWelcome back, {self.name}! You have {len(self.expenses)} expense record(s).\n")

    def show_menu(self) -> None:
        """Display the main menu and handle user choices."""
        while True:
            print("\n" + "=" * 40)
            print("         EXPENSE TRACKER")
            print("=" * 40)
            print("1. Set Monthly Budget")
            print("2. Add Expense")
            print("3. View All Expenses")
            print("4. View Summary")
            print("5. Analyze Spending")
            print("6. Edit / Delete Expense")
            print("7. Export Expenses to CSV")
            print("0. Exit")
            print("=" * 40)

            try:
                choice = int(input("Enter Your Choice: "))
            except ValueError:
                print(f"{self.name}, Please enter a valid number.")
                continue

            actions = {
                0: self.exit_app,
                1: self.set_budget,
                2: self.add_expense,
                3: self.view_expenses,
                4: self.view_summary,
                5: self.analyze_spending,
                6: self.edit_delete_expense,
                7: self.export_csv,
            }
            action = actions.get(choice)
            if action:
                action()
            else:
                print(f"{self.name}, Please enter a valid choice (0-7).")

    def set_budget(self) -> None:
        """Set or update the monthly budget."""
        try:
            amount = float(input(f"{self.name}, Enter Your Monthly Budget: $"))
            if amount <= 0:
                print("Budget must be greater than zero.")
                return
            self.monthly_budget = amount
            print(f"✅ Monthly budget of ${amount:.2f} has been set!")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def add_expense(self) -> None:
        """Add a new expense record."""
        print(f"\n--- Add New Expense ---")
        title = input("Expense Title: ").strip()
        if not title:
            print("❌ Title cannot be empty.")
            return

        # Show categories
        print("\nCategories:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"  {i}. {cat}")
        try:
            cat_choice = int(input("Choose category (1-8): "))
            if cat_choice < 1 or cat_choice > len(CATEGORIES):
                print("❌ Invalid category choice.")
                return
            category = CATEGORIES[cat_choice - 1]
        except ValueError:
            print("❌ Invalid input.")
            return

        try:
            amount = float(input("Expense Amount: $"))
            if amount <= 0:
                print("❌ Amount must be positive.")
                return
        except ValueError:
            print("❌ Invalid amount.")
            return

        today = datetime.now().strftime("%Y-%m-%d")
        expense = {
            "date": today,
            "category": category,
            "title": title,
            "amount": f"{amount:.2f}",
        }
        self.expenses.append(expense)
        save_expenses(self.expenses)

        total_spent = sum(float(e["amount"]) for e in self.expenses)
        if self.monthly_budget > 0:
            remaining = self.monthly_budget - total_spent
            print(f"\n✅ Expense added! Budget remaining: ${remaining:.2f} / ${self.monthly_budget:.2f}")
            if remaining < 0:
                print("⚠️  You have exceeded your monthly budget!")
        else:
            print(f"\n✅ Expense added! (Set a budget to track remaining balance.)")

    def view_expenses(self) -> None:
        """Display all expenses in a table."""
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return

        print("\n" + "=" * 70)
        print(f"{'#':<3} {'Date':<12} {'Category':<15} {'Title':<20} {'Amount':<8}")
        print("=" * 70)
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i:<3} {exp['date']:<12} {exp['category']:<15} {exp['title']:<20} ${float(exp['amount']):<7.2f}")
        print("=" * 70)

        total = sum(float(e["amount"]) for e in self.expenses)
        print(f"{'':>38} Total: ${total:.2f}")

    def view_summary(self) -> None:
        """Show a quick summary of finances."""
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return

        total_spent = sum(float(e["amount"]) for e in self.expenses)
        print(f"\n--- Budget Summary for {self.name} ---")
        print(f"Total Expenses: ${total_spent:.2f}")
        if self.monthly_budget > 0:
            print(f"Monthly Budget: ${self.monthly_budget:.2f}")
            remaining = self.monthly_budget - total_spent
            print(f"Remaining:      ${remaining:.2f}")
            if remaining >= 0:
                print(f"✅ You are within budget by ${remaining:.2f}")
            else:
                print(f"⚠️  You are over budget by ${abs(remaining):.2f}")
        else:
            print("ℹ️  Set a monthly budget to track spending limits.")

        # Category breakdown
        print(f"\nSpending by Category:")
        cat_totals: Dict[str, float] = {}
        for exp in self.expenses:
            cat = exp["category"]
            cat_totals[cat] = cat_totals.get(cat, 0) + float(exp["amount"])
        for cat, amt in sorted(cat_totals.items(), key=lambda x: x[1], reverse=True):
            pct = (amt / total_spent) * 100 if total_spent > 0 else 0
            print(f"  {cat:<15} ${amt:<8.2f} ({pct:.1f}%)")

    def analyze_spending(self) -> None:
        """Detailed spending analysis with monthly breakdown."""
        if not self.expenses:
            print("📭 No expenses recorded yet. Add some expenses first!")
            return

        print(f"\n{'=' * 50}")
        print(f"          SPENDING ANALYSIS")
        print(f"{'=' * 50}")

        # Group by month
        monthly: Dict[str, List[Dict]] = {}
        for exp in self.expenses:
            month = exp["date"][:7]  # YYYY-MM
            monthly.setdefault(month, []).append(exp)

        print(f"\nMonthly Breakdown:")
        for month in sorted(monthly.keys(), reverse=True):
            month_exps = monthly[month]
            month_total = sum(float(e["amount"]) for e in month_exps)
            print(f"\n  📅 {month}: ${month_total:.2f} ({len(month_exps)} expenses)")

            # Per category
            cat_totals: Dict[str, float] = {}
            for e in month_exps:
                cat_totals[e["category"]] = cat_totals.get(e["category"], 0) + float(e["amount"])
            for cat, amt in sorted(cat_totals.items(), key=lambda x: x[1], reverse=True):
                bar = "█" * int((amt / month_total) * 20) if month_total > 0 else ""
                print(f"    {cat:<12} ${amt:<7.2f} {bar}")

        # Top expenses
        print(f"\nTop 5 Highest Expenses:")
        sorted_expenses = sorted(self.expenses, key=lambda e: float(e["amount"]), reverse=True)[:5]
        for i, exp in enumerate(sorted_expenses, 1):
            print(f"  {i}. ${float(exp['amount']):<7.2f} - {exp['title']} ({exp['date']})")

    def edit_delete_expense(self) -> None:
        """Edit or delete an existing expense."""
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return

        self.view_expenses()
        try:
            idx = int(input(f"\nEnter the # of the expense to edit/delete (0 to cancel): "))
            if idx == 0:
                return
            if idx < 1 or idx > len(self.expenses):
                print("❌ Invalid expense number.")
                return
        except ValueError:
            print("❌ Invalid input.")
            return

        exp = self.expenses[idx - 1]
        print(f"\nSelected: [{exp['date']}] {exp['category']} - {exp['title']} - ${float(exp['amount']):.2f}")
        action = input("What would you like to do? (E)dit / (D)elete / (C)ancel: ").strip().upper()

        if action == "D":
            confirm = input(f"Are you sure you want to delete this expense? (y/N): ").strip().upper()
            if confirm == "Y":
                self.expenses.pop(idx - 1)
                save_expenses(self.expenses)
                print("✅ Expense deleted.")
        elif action == "E":
            print("\n--- Editing Expense (press Enter to keep current value) ---")
            new_date = input(f"Date [{exp['date']}]: ").strip()
            if new_date:
                exp["date"] = new_date

            print("Categories:", ", ".join(f"{i+1}.{CATEGORIES[i]}" for i in range(len(CATEGORIES))))
            cat_input = input(f"Category [{exp['category']}]: ").strip()
            if cat_input:
                try:
                    cat_num = int(cat_input)
                    if 1 <= cat_num <= len(CATEGORIES):
                        exp["category"] = CATEGORIES[cat_num - 1]
                    else:
                        print("Invalid category number, keeping original.")
                except ValueError:
                    exp["category"] = cat_input

            new_title = input(f"Title [{exp['title']}]: ").strip()
            if new_title:
                exp["title"] = new_title

            new_amount = input(f"Amount [{float(exp['amount']):.2f}]: ").strip()
            if new_amount:
                try:
                    amt = float(new_amount)
                    if amt > 0:
                        exp["amount"] = f"{amt:.2f}"
                    else:
                        print("Amount must be positive, keeping original.")
                except ValueError:
                    print("Invalid amount, keeping original.")

            save_expenses(self.expenses)
            print("✅ Expense updated.")
        else:
            print("Cancelled.")

    def export_csv(self) -> None:
        """Export expenses to a timestamped CSV file."""
        if not self.expenses:
            print("📭 No expenses to export.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"expense_report_{timestamp}.csv"
        try:
            with open(filename, "w", newline="") as f:
                fieldnames = ["date", "category", "title", "amount"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.expenses)
            print(f"✅ Exported to {filename}")
        except IOError:
            print(f"❌ Failed to export to {filename}")

    def exit_app(self) -> None:
        """Exit the application gracefully."""
        print(f"\nThank you for using Expense Tracker, {self.name}!")
        print("Your data has been saved. Goodbye! 👋")
        exit(0)


if __name__ == "__main__":
    try:
        app = Budget()
        app.show_menu()
    except KeyboardInterrupt:
        print("\n\nExiting... Your data is safe. Goodbye!")

