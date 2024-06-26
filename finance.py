import argparse
from DB import DB  # Importing the database module

# Initialize the database
DB = DB()
DB.update()

class Finance:
    def __init__(self):
        self.income_statement = {}
        self.profit_list = []
        self.expenses_dict = {'coach': {}, 'hall': {}, 'utilities': {}, 'events': {}}
        self.revenue_dict = {}

    # Method to add revenue to the income statement and dictionary
    def add_revenue(self, month, amount):
        if 'revenue' not in self.income_statement:
            self.income_statement['revenue'] = {}
        self.income_statement['revenue'][month] = amount
        if month not in self.revenue_dict:
            self.revenue_dict[month] = amount
        else:
            self.revenue_dict[month] += amount

    # Method to add expenses to the income statement and dictionary
    def add_expenses(self, month, category, amount):
        if category not in self.expenses_dict:
            self.expenses_dict[category] = {}
        if month not in self.expenses_dict[category]:
            self.expenses_dict[category][month] = amount
        else:
            self.expenses_dict[category][month] += amount

    # Method to add monthly profit to the profit list
    def add_monthly_profit(self, month, profit):
        self.profit_list.append((month, profit))

    # Method to get the total unpaid expenses
    def get_total_unpaid_expenses(self):
        total_coach_expenses = sum(expense for month, expense in self.expenses_dict.get('coach', {}).items())
        total_hall_expenses = sum(expense for month, expense in self.expenses_dict.get('hall', {}).items())
        total_utilities_expenses = sum(expense for month, expense in self.expenses_dict.get('utilities', {}).items())
        total_event_expenses = sum(expense for month, expense in self.expenses_dict.get('events', {}).items())
        return total_coach_expenses, total_hall_expenses, total_utilities_expenses, total_event_expenses

    # Method to record transactions
    def record_transaction(self, transaction):
        if 'transactions' not in self.income_statement:
            self.income_statement['transactions'] = []
        self.income_statement['transactions'].append(transaction)

    # Method to retrieve the current month's account payables
    def get_current_month_account_payables(self, month):
        # Calculate account payables based on revenues recorded for the current month
        current_month_revenue = self.income_statement['revenue'].get(month, 0)
        return current_month_revenue

    # Method to save changes to the database
    def save_to_database(self):
        DB.save()

    # Method to output all expenses for each month in tabular form
    def output_expenses_table(self):
        print("\nExpenses for Each Month:")
        print("Month    | Coach Expenses | Hall Expenses | Utilities Expenses | Event Expenses")
        print("-------------------------------------------------------------------------------")
        for month in self.expenses_dict['coach']:
            coach_expenses = self.expenses_dict['coach'].get(month, 0)
            hall_expenses = self.expenses_dict['hall'].get(month, 0)
            utilities_expenses = self.expenses_dict['utilities'].get(month, 0)
            event_expenses = self.expenses_dict['events'].get(month, 0)
            print(f"{month} | {coach_expenses} | {hall_expenses} | {utilities_expenses} | {event_expenses}")
        print("-------------------------------------------------------------------------------")

    # Method to output all revenue for each month in tabular form
    def output_revenue_table(self):
        print("\nRevenue for Each Month:")
        print("Month    | Revenue")
        print("-------------------")
        for month, revenue in self.revenue_dict.items():
            print(f"{month} | {revenue}")
        print("-------------------")


# Function to calculate finances based on provided data
def calculate_finances(data):
    total_revenue = 0
    total_expenses = 0
    unpaid_debt = 0

    for session in data:
        price_per_member = session["price"]
        num_members = sum(1 for member in session["members"] if member["paid"])
        revenue = price_per_member * num_members
        total_revenue += revenue

        if session["coach_attended"]:
            coach_cut = revenue * 0.2  # Assuming 20% cut for the coach
            total_expenses += coach_cut

        rent_expense = 200  # Example rent expense
        total_expenses += rent_expense

        utilities_expense = 50  # Example utilities expense
        total_expenses += utilities_expense

        event_expense = 100  # Example event expense
        total_expenses += event_expense

        unpaid_fees = price_per_member * sum(1 for member in session["members"] if not member["paid"])
        unpaid_debt += unpaid_fees

    profit = total_revenue - total_expenses

    return total_revenue, total_expenses, profit, unpaid_debt


def main():
    finance = Finance()

    print("\nClub Finances Management Menu:")
    print("[1] Add Revenue")
    print("[2] Add Expenses")
    print("[3] Add Monthly Profit")
    print("[4] Get Total Unpaid Expenses")
    print("[5] Record Transaction")
    print("[6] Get Current Month's Account Payables")
    print("[7] Output Expenses Table")
    print("[8] Output Revenue Table")
    print("[9] Save to Database")
    print("[10] Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            month = input("Enter month: ")
            amount = float(input("Enter revenue amount: "))
            finance.add_revenue(month, amount)
            finance.save_to_database()

        elif choice == "2":
            month = input("Enter month: ")
            category = input("Enter category (coach/hall/utilities/events): ")
            amount = float(input("Enter expenses amount: "))
            finance.add_expenses(month, category, amount)
            finance.save_to_database()

        elif choice == "3":
            month = input("Enter month: ")
            profit = float(input("Enter profit: "))
            finance.add_monthly_profit(month, profit)
            finance.save_to_database()

        elif choice == "4":
            coach_expenses, hall_expenses, utilities_expenses, event_expenses = finance.get_total_unpaid_expenses()
            print(f"Total Unpaid Coach Expenses: {coach_expenses}")
            print(f"Total Unpaid Hall Expenses: {hall_expenses}")
            print(f"Total Utilities Expenses: {utilities_expenses}")
            print(f"Total Event Expenses: {event_expenses}")

        elif choice == "5":
            transaction = input("Enter transaction: ")
            finance.record_transaction(transaction)
            finance.save_to_database()

        elif choice == "6":
            month = input("Enter month: ")
            account_payables = finance.get_current_month_account_payables(month)
            print(f"Account Payables for {month}: {account_payables}")

        elif choice == "7":
            finance.output_expenses_table()

        elif choice == "8":
            finance.output_revenue_table()

        elif choice == "9":
            finance.save_to_database()
            print("Changes saved to database.")

        elif choice == "10":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
