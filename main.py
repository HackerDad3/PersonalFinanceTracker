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
    start_date = input("Enter the start date (yyyy-mm-dd): ")
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
    print("Feature: View Weekly Breakdown (coming soon)")

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
