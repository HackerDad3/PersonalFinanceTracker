# **Personal Finance Tracker Plan**

## **Goals**
1. Automate the tracking of yearly, monthly, and weekly expenses and income.
2. Provide insights into account balances and ensure sufficient funds for upcoming bills.
3. Replace manual spreadsheet calculations with an intuitive Python-based solution.

---

## **Core Features**
### **1. Yearly Expense and Income Tracking**
- **Purpose**: Automate the yearly schedule of expenses and income based on user input.
- **Details**:
  - Allow input of recurring expenses (e.g., fortnightly, monthly, once-off).
  - Automatically populate a yearly schedule with calculated dates and amounts.
  - Include categories (e.g., Rent, Food, Entertainment) and associated accounts.

### **2. Monthly Overview**
- **Purpose**: Summarize income and expenses for a selected month.
- **Details**:
  - Generate a monthly sheet from the yearly data.
  - Show all scheduled transactions for that month.
  - Categorize by accounts and highlight totals.

### **3. Weekly Breakdown**
- **Purpose**: Provide a focused view of income and expenses for a selected week.
- **Details**:
  - Extract weekly data from the monthly sheet.
  - Display scheduled transactions and their impact on account balances.
  - Highlight potential issues (e.g., insufficient funds).

### **4. Account Balances and Projections**
- **Purpose**: Ensure enough money is available for upcoming bills.
- **Details**:
  - Calculate required balances for each account.
  - Project account balances across multiple weeks to the next pay cycle.
  - Flag weeks with potential shortfalls or surpluses.

---

## **Advanced Features (Future Goals)**
1. **Manual Adjustments**:
   - Allow users to modify scheduled transactions (e.g., adjust dates or amounts).
2. **Data Visualization**:
   - Generate charts to show trends in spending, income, and account balances.
3. **Import/Export**:
   - Import existing spreadsheet data or export reports in CSV format.
4. **Mobile/Desktop Integration**:
   - Extend functionality to a mobile or desktop application.
5. **Special Budgets**:
   - Have micro budgets for special events like Christmas or other holidays.

---

## **Program Flow**
1. **Menu System**:
   - Main menu with options:
     ```
     1. Add Recurring Expense/Income
     2. View Yearly Schedule
     3. View Monthly Overview
     4. View Weekly Breakdown
     5. Check Account Projections
     6. Exit
     ```

2. **Features Implementation**:
   - **Add Recurring Expense/Income**:
     - Input: Name, amount, category, frequency (e.g., fortnightly, monthly), account.
     - Automatically calculate and populate dates/amounts in the yearly schedule.
   - **View Yearly Schedule**:
     - Display the full year’s data.
   - **View Monthly Overview**:
     - Filter data for the selected month.
   - **View Weekly Breakdown**:
     - Filter data for the selected week and show account adequacy.
   - **Check Account Projections**:
     - Summarize balances across weeks up to the next pay cycle.

---

## **Data Structure**
### **Recurring Transactions**
```python
recurring_transactions = [
    {
        "name": "Rent",
        "amount": 1200,
        "category": "Housing",
        "frequency": "fortnightly",
        "start_date": "2024-01-02",
        "account": "Main Account"
    },
    # Additional transactions
]
