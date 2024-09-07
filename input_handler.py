def add_expense(expense_list):
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter expense category (e.g., Food, Transport): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        expense_list.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid numbers and data.")
