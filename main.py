# Personal Finance Tracker

__version__ = "0.1.0"

# Imports
from datetime import datetime, timedelta

# Define all the functions first.  There are the current features we want to use.
recurring_transactions = []

def add_recurring_transaction():
    """Collect details for a recurring transaction and add it to the list"""
    print("\nAdd Recurring Transaction")

    # Collect transaction details
    name = input("Enter the name of the transaction (e.g. Rent): ")
    amount = float(input("Enter the amount (e.g. 1200): "))
    category = input("Enter the category (e.g. Housing, Food): ")
    frequency = input("Enter the frequency (e.g. weekly, monthly, fortnightly): ")
    # start_date = input("Enter the start date (yyyy-mm-dd): ")

    # Validate date
    while True:
        start_date_str = input("Enter the start date (dd-mm-yyyy): ")
        try:
            start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY")
            
    account = input("Enter the account (e.g. Main Account, Savings Account): ")

    # Create a dict for the transactions
    transaction = {
        "name": name,
        "amount": amount,
        "category": category,
        "frequency": frequency,
        "start_date": start_date,
        "account": account
    }

    # Add the transaction to the list
    recurring_transactions.append(transaction)
    print(f"Transaction '{name}' added successfully!")

def view_yearly_schedule():
    """Display all recurring transactions for the year."""
    print("\nYearly Schedule")
    if not recurring_transactions:
        print("No transactions found.")
        return
    
    # Loop through the transactions and display them.
    for i, transaction in enumerate(recurring_transactions, start=1):
        print(f"\nTransaction {i}:")
        print(f"  Name: {transaction['name']}")
        print(f"  Amount: ${transaction['amount']:.2f}")
        print(f"  Category: {transaction['category']}")
        print(f"  Frequency: {transaction['frequency']}")
        print(f"  Start Date: {transaction['start_date']}")
        print(f"  Account: {transaction['account']}")

def view_monthly_overview():
    """Display transactions for a specific month."""
    print("\nMonthly Overview")
    if not recurring_transactions:
        print("No transactions found.")
        return

    # Get the desired month and year from the user
    year = int(input("Enter the year (e.g., 2024): "))
    month = int(input("Enter the month (1-12): "))

    # Start and end dates for the selected month
    start_of_month = datetime(year, month, 1)
    if month == 12:  # Handle December separately
        end_of_month = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_of_month = datetime(year, month + 1, 1) - timedelta(days=1)

    print(f"\nTransactions for {start_of_month.strftime('%B %Y')}:")
    found = False

    # Filter and display transactions
    for transaction in recurring_transactions:
        transaction_date = datetime.strptime(transaction['start_date'], "%Y-%m-%d")
        frequency = transaction['frequency'].lower()

        # Check if the transaction falls within the month
        while transaction_date <= end_of_month:
            if start_of_month <= transaction_date <= end_of_month:
                print(f"\n  Name: {transaction['name']}")
                print(f"  Amount: ${transaction['amount']:.2f}")
                print(f"  Category: {transaction['category']}")
                print(f"  Frequency: {transaction['frequency']}")
                print(f"  Scheduled Date: {transaction_date.strftime('%Y-%m-%d')}")
                print(f"  Account: {transaction['account']}")
                found = True

            # Move to the next scheduled date
            if frequency == "weekly":
                transaction_date += timedelta(weeks=1)
            elif frequency == "fortnightly":
                transaction_date += timedelta(weeks=2)
            elif frequency == "monthly":
                transaction_date += timedelta(days=30)  # Approximation
            else:
                break  # Once-off transactions only repeat once

    if not found:
        print("No transactions found for this month.")

def view_weekly_breakdown():
    """Display a detailed breakdown of transactions for a specific week."""
    print("\nWeekly Breakdown")
    if not recurring_transactions:
        print("No transactions found.")
        return

    # Get the start date of the week from the user
    start_date_str = input("Enter the start date of the week (YYYY-MM-DD): ")
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Calculate the end date of the week
    end_date = start_date + timedelta(days=6)

    print(f"\nTransactions for the week {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}:")
    found = False

    # Initialize totals
    total_income = 0
    total_expenses = 0
    account_balances = {}

    # Filter and display transactions
    for transaction in recurring_transactions:
        transaction_date = datetime.strptime(transaction['start_date'], "%Y-%m-%d")
        frequency = transaction['frequency'].lower()

        # Check if the transaction falls within the week
        while transaction_date <= end_date:
            if start_date <= transaction_date <= end_date:
                amount = transaction['amount']
                account = transaction['account']
                category = transaction['category']

                # Income vs Expense logic (can adjust based on category or type)
                if category.lower() in ["income", "salary", "paycheck"]:
                    total_income += amount
                else:
                    total_expenses += amount

                # Track balances by account
                if account not in account_balances:
                    account_balances[account] = 0
                account_balances[account] += amount if category.lower() in ["income", "salary"] else -amount

                # Display transaction details
                print(f"\n  Name: {transaction['name']}")
                print(f"  Amount: ${amount:.2f}")
                print(f"  Category: {category}")
                print(f"  Scheduled Date: {transaction_date.strftime('%Y-%m-%d')}")
                print(f"  Account: {account}")
                found = True

            # Move to the next scheduled date
            if frequency == "weekly":
                transaction_date += timedelta(weeks=1)
            elif frequency == "fortnightly":
                transaction_date += timedelta(weeks=2)
            elif frequency == "monthly":
                transaction_date += timedelta(days=30)  # Approximation
            else:
                break  # Once-off transactions only repeat once

    if not found:
        print("No transactions found for this week.")
    else:
        # Display weekly totals
        print("\nWeekly Summary:")
        print(f"  Total Income: ${total_income:.2f}")
        print(f"  Total Expenses: ${total_expenses:.2f}")
        print(f"  Net Balance: ${total_income - total_expenses:.2f}")

        # Display account balances and highlight potential shortfalls
        print("\nAccount Balances:")
        for account, balance in account_balances.items():
            status = "OK" if balance >= 0 else "INSUFFICIENT FUNDS"
            print(f"  {account}: ${balance:.2f} ({status})")


def manage_special_budgets():
    print("Feature: Manage Special Budgets (coming soon)")

def check_account_projections():
    print("Feature: Check Account Projections (coming soon)")

# Define the main function last
def main():
    while True:
        print("\nWelcome to Personal Finance Tracker!")
        print("1. Add Recurring Expense/Income")
        print("2. View Yearly Schedule")
        print("3. View Monthly Overview")
        print("4. View Weekly Breakdown")
        print("5. Manage Special Budgets")
        print("6. Check Account Projections")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_recurring_transaction()
        elif choice == "2":
            view_yearly_schedule()
        elif choice == "3":
            view_monthly_overview()
        elif choice == "4":
            view_weekly_breakdown()
        elif choice == "5":
            manage_special_budgets()
        elif choice == "6":
            check_account_projections()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program by calling main
if __name__ == "__main__":
    main()
