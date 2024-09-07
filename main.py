from input_handler import add_expense
from data_manager import load_expenses, save_expenses
from analysis import monthly_summary, category_summary
from interface import display_menu

def main():
    expenses = load_expenses()
    while True:
        choice = display_menu()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            monthly_summary(expenses)
        elif choice == '3':
            category_summary(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
