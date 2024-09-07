categories = ["Food", "Transport", "Entertainment", "Miscellaneous"]

def choose_category():
    print("Choose a category:")
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")
    choice = int(input("Enter the number: "))
    return categories[choice - 1]
