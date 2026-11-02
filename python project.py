import json

transactions = []

try:
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
except FileNotFoundError:
    pass

while True:
    print("===== Personal Finance Management System =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. Summary")
    print("5. Search")
    print("6. Delete Transaction")
    print("7. Exit")
    print("8. Clear All Transactions")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Income selected")
        amount = input("Enter income amount: ")
        source = input("Enter income source: ")

        transactions.append(("Income", amount, source))

        with open("transactions.json", "w") as file:
            json.dump(transactions, file)

    elif choice == "2":
        print("Add Expense selected")
        amount = input("Enter expense amount: ")
        category = input("Enter expense category: ")

        transactions.append(("Expense", amount, category))

        with open("transactions.json", "w") as file:
            json.dump(transactions, file)

    elif choice == "3":
        print("View All Transactions selected")

        for transaction in transactions:
            print(transaction)

    elif choice == "4":
        print("Summary selected")
        total_income = 0
        total_expense = 0

        for transaction in transactions:
            if transaction[0] == "Income":
                total_income += float(transaction[1])
            else:
                total_expense += float(transaction[1])

        print("Total Income:", total_income)
        print("Total Expense:", total_expense)
        print("Balance:", total_income - total_expense)

    elif choice == "5":
        print("Search selected")
        search_item = input("Enter source or category to search: ")

        for transaction in transactions:
            if transaction[2].lower() == search_item.lower():
                if transaction[0] == "Income":
                    print(transaction[2], "+₹" + transaction[1])
                else:
                    print(transaction[2], "-₹" + transaction[1])

    elif choice == "6":
        print("Delete Transaction selected")
        delete_item = input("Enter source or category to delete: ")

        for transaction in transactions:
            if transaction[2].lower() == delete_item.lower():
                transactions.remove(transaction)

                with open("transactions.json", "w") as file:
                    json.dump(transactions, file)

                print("Transaction deleted successfully")
                break

    elif choice == "7":
        print("Exiting program...")
        break

    elif choice == "8":
        print("Clear All Transactions selected")
        confirm = input("Are you sure you want to clear all transactions? (yes/no): ")

        if confirm.lower() == "yes":
            transactions.clear()

            with open("transactions.json", "w") as file:
                json.dump(transactions, file)

            print("All transactions cleared successfully!")
        else:
            print("Clear operation cancelled.")

    else:
        print("Invalid choice")



   
