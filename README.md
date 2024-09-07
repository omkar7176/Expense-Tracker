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



<h1>Installation</h1>
