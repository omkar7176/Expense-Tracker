# Expense Tracker

The **Expense Tracker** is a Python-based application that allows users to track their daily expenses, categorize them, and analyze their spending patterns. This project is developed as part of a Python Programming internship and helps users manage their finances efficiently.

## Features
- **User Input**: Add daily expenses with details like date, category, amount, and description.
- **Data Storage**: All expense data is saved in a `JSON` file for persistence.
- **Expense Categories**: Organize expenses into different categories (e.g., Food, Transport, Entertainment, etc.).
- **Monthly Summary**: Analyze total spending for each month.
- **Category-wise Summary**: View total expenses by category.
- **Error Handling**: Handles invalid inputs and unexpected errors gracefully.
- **User-Friendly CLI**: Easy-to-use command-line interface for adding, viewing, and saving expenses.
- **Modular Structure**: The project is divided into multiple files for better maintainability.

## Project Structure

```plaintext
expense_tracker/
│
├── main.py                  # Main entry point for the application
├── input_handler.py          # Handles user input and adding expenses
├── data_manager.py           # Manages saving and loading expense data
├── analysis.py               # Functions for expense analysis (monthly, category-wise)
├── interface.py              # Command-line interface for user interaction
└── categories.py             # Handles predefined expense categories

```

## Installation

**1. Clone the repository:**  git clone https://github.com/your-username/expense-tracker.git<br/>
**2. Navigate to the project directory:**  cd Expense-Tracker<br/>
**3. Run the application:**  python main.py



## Usage

**1. Once the application is running, you will be prompted with a menu:**<br/>
**2. Add a new expense.**<br/>
**3. View a summary of your monthly expenses.**<br/>
**4. View a summary of expenses by category.**<br/>
**5. Save the data and exit the application.**<br/>
**6. Example of adding an expense:**

```plaintext
Enter date (YYYY-MM-DD): 2024-09-01
Enter expense category (e.g., Food, Transport): Food
Enter amount: 10.50
Enter description: Lunch at a restaurant
Expense added successfully!

```
**Example of viewing a summary:**
```plaintext
Expense Tracker Menu:
1. Add Expense
2. View Monthly Summary
3. View Category Summary
4. Save and Exit
Enter choice: 2

Total spent in 2024-09: 150.75

```
## Contributing
```plaintext
If you'd like to contribute, feel free to fork the repository and submit a pull request. Any suggestions or improvements are welcome!