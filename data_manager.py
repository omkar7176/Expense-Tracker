import json

def save_expenses(expense_list, filename="expenses.json"):
    with open(filename, 'w') as file:
        json.dump(expense_list, file)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
