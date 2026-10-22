print("PERSONAL EXPENSE TRACKER")

budget = float(input("Enter your budget: "))

expenses = []

while True:
    print("\n--- MENU ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Check Remaining Budget")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("What did you spend money on? ")
        amount = float(input("Enter amount spent: "))

        if amount <= 0:
            print("Invalid amount! Enter an amount greater than zero.")
        else:
            expense = {
                "name": name,
                "amount": amount
            }

            expenses.append(expense)
            print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n--- YOUR EXPENSES ---")

            for expense in expenses:
                print(expense["name"], "-", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total Spending:", total)

    elif choice == "4":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        remaining = budget - total

        print("Your Budget:", budget)
        print("Total Spending:", total)
        print("Remaining Budget:", remaining)

        if remaining < 0:
            print("Warning: You have exceeded your budget!")

    elif choice == "5":
        print("Thank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice! Please select an option from 1 to 5.")