from collections import defaultdict

def monthly_summary(expense_list):
    summary = defaultdict(float)
    for expense in expense_list:
        month = expense["date"][:7]  # Extract YYYY-MM for monthly grouping
        summary[month] += expense["amount"]
    for month, total in summary.items():
        print(f"Total spent in {month}: {total}")

def category_summary(expense_list):
    summary = defaultdict(float)
    for expense in expense_list:
        summary[expense["category"]] += expense["amount"]
    for category, total in summary.items():
        print(f"Total spent on {category}: {total}")
