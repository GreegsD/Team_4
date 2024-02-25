class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
def add_transaction():
    date = input("Введіть дату транзакції (YYYY-MM-DD): ")
    amount = float(input("Введіть суму транзакції: "))
    category = input("Введіть категорію транзакції (дохід/витрата): ")
    description = input("Введіть опис транзакції: ")

    return Transaction(date, amount, category, description)
transactions = []
while True:
    answer = input("Ввести ще транзакцію? (y/n): ")
    if answer.lower() == "n":
        break
    transactions.append(add_transaction())

def get_categories(transactions):
    categories = set()
    for transaction in transactions:
        categories.add(transaction.category)
    return categories

categories = get_categories(transactions)
def calculate_total_expenses(transactions):
    total_expenses = 0
    for transaction in transactions:
        if transaction.category == "Витрата":
            total_expenses += transaction.amount
    return total_expenses

total_expenses = calculate_total_expenses(transactions)
def print_report(categories, total_expenses):
    print("Звіт про витрати")
    print("-----------------")
    for category in categories:
        print(f"{category}:")
        for transaction in transactions:
            if transaction.category == category:
                print(f"    - {transaction.date}: {transaction.amount} ({transaction.description})")
    print("-----------------")
    print(f"Загальні витрати: {total_expenses}")

print_report(categories, total_expenses)
