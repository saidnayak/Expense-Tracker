import json
import os
from datetime import datetime

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: expenses.json corrupted. Starting fresh.")
            return []
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Enter category (e.g. Food, Transport): ").strip()
    description = input("Enter description: ").strip()
    date_str = input("Enter date (YYYY-MM-DD) or leave empty for today: ").strip()
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format.")
            return
    else:
        date = datetime.today().date()

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": str(date)
    }
    expenses.append(expense)
    print("Expense added.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpenses:")
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. ${exp['amount']:.2f} - {exp['category']} - {exp['description']} - {exp['date']}")

def total_expenses(expenses):
    total = sum(exp.get("amount", 0) for exp in expenses)
    print(f"\nTotal expenses: ${total:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
