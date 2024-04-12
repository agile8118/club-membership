import argparse
from DB import DB  # Importing the database module

# Initialize the database
DB = DB()
DB.update()

class Finance:
    def __init__(self):
        self.income_statement = {}
        self.profit_list = []

    # Method to add revenue to the income statement
    def add_revenue(self, revenue):
        self.income_statement['revenue'] = revenue

    # Method to add expenses to the income statement
    def add_expenses(self, expenses):
        self.income_statement['expenses'] = expenses

    # Method to log monthly profit
    def log_monthly_profit(self, month, profit):
        self.profit_list.append((month, profit))

    # Method to log unpaid debt for a specific month
    def log_unpaid_debt(self, month, unpaid_debt):
        self.income_statement['unpaid_debt'] = {month: unpaid_debt}

    # Method to log account payables for a specific month
    def log_account_payables(self, month, account_payables):
        self.income_statement['account_payables'] = {month: account_payables}

    # Method to save changes to the database
    def save_to_database(self):
        DB.save()

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

        unpaid_fees = price_per_member * sum(1 for member in session["members"] if not member["paid"])
        unpaid_debt += unpaid_fees

    profit = total_revenue - total_expenses

    return total_revenue, total_expenses, profit, unpaid_debt


def main():
    # Define command-line arguments
    parser = argparse.ArgumentParser(description='Manage club finances.')
    parser.add_argument('action', choices=['revenue', 'expenses', 'profit', 'unpaid_debt', 'account_payables'],
                        help='Action to perform: revenue, expenses, profit, unpaid_debt, account_payables')
    parser.add_argument('--month', help='Month for logging/unpaid debt/account payables')
    parser.add_argument('--revenue', type=int, help='Total revenue amount')
    parser.add_argument('--expenses', type=int, help='Total expenses amount')
    parser.add_argument('--profit', type=int, help='Monthly profit amount')
    parser.add_argument('--coach_expenses', type=int, help='Total unpaid coach expenses')
    parser.add_argument('--hall_expenses', type=int, help='Total unpaid hall expenses')

    args = parser.parse_args()

    finance = Finance()

    print("Performing action:", args.action)

    # Perform the requested action based on the provided arguments
    if args.action == 'revenue':
        print("Adding revenue:", args.revenue)
        finance.add_revenue(args.revenue)
        finance.save_to_database()
        print("Revenue added and saved to database.")

    elif args.action == 'expenses':
        print("Adding expenses:", args.expenses)
        finance.add_expenses(args.expenses)
        finance.save_to_database()
        print("Expenses added and saved to database.")

    elif args.action == 'profit':
        print("Logging monthly profit for", args.month, ":", args.profit)
        finance.log_monthly_profit(args.month, args.profit)
        finance.save_to_database()
        print("Monthly profit logged and saved to database.")

    elif args.action == 'unpaid_debt':
        total_unpaid_debt = args.coach_expenses + args.hall_expenses
        print("Logging unpaid debt for", args.month, ":", total_unpaid_debt)
        finance.log_unpaid_debt(args.month, total_unpaid_debt)
        finance.save_to_database()
        print("Unpaid debt logged and saved to database.")

    elif args.action == 'account_payables':
        month_data = DB.get_month_data(args.month)
        total_unpaid_fees = sum(session["price"] * (len(session["members"]) - sum(member["paid"] for member in session["members"])) for session in month_data)
        print("Calculating account payables for", args.month, ":", total_unpaid_fees)
        finance.log_account_payables(args.month, total_unpaid_fees)
        finance.save_to_database()
        print("Account payables calculated and saved to database.")


if __name__ == "__main__":
    main()

