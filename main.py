# Personal Finance Tracker

__version__ = "0.1.0"

# Define all the functions first.  There are the current features we want to use.
recurring_transactions = []

def add_recurring_transaction():
    print("\nAdd Recurring Transaction")

    # Collect transaction details
    name = input("Enter the name of the transaction (e.g. Rent): ")
    amount = input("Enter the amount (e.g. 1200): ")
    category = input("Enter the category (e.g. Housing, Food): ")
    frequency = input("Enter the frequency (e.g. weekly, monthly, fortnightly): ")
    start_date = input("Enter the start date (dd-mm-yyyy): ")
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
    print("Feature: View Yearly Schedule (coming soon)")

def view_monthly_overview():
    print("Feature: View Monthly Overview (coming soon)")

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
