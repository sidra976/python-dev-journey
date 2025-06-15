import json
import os

FILE_NAME = 'expense_manager.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        return []

def save_tasks(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file)

def view_expense_list(expenses):
    if not expenses:
        print('Expense Unavailable!')
    for index, expense in enumerate(expenses, start=1):
        print(f'{index} Expense Name: {expense["Expense_name"]} Amount: {expense["Amount"]} Date: {expense["Date"]}')

def view_total_expense(expenses):
    total_expense = sum(item["Amount"] for item in expenses)
    print(f'Total Expense: {total_expense}')

def add_expense(expenses):
    expense_name = input('Add expense name: ')
    amount = float(input('Add amount: '))
    date = input('Add date: ')
    expenses.append({"Expense_name": expense_name, "Amount": amount, "Date": date})
    save_tasks(expenses)

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return
    view_expense_list(expenses)
    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_tasks(expenses)
            print(f"Deleted: {removed['Expense_name']} | Amount: {removed['Amount']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    expenses = load_tasks()
    while True:
        print('\nExpense Tracker App')
        print('1. View full expense list')
        print('2. View total expense')
        print('3. Add Expense')
        print('4. Delete Expense')
        print('5. Exit')
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                view_expense_list(expenses)
            case '2':
                view_total_expense(expenses)
            case '3':
                add_expense(expenses)
                expenses = load_tasks()  # Reload expenses
            case '4':
                delete_expense(expenses)
                expenses = load_tasks()  # Reload expenses
            case '5':
                print("Exiting. Goodbye!")
                break
            case _:
                print('Invalid choice')

if __name__ == '__main__':
    main()

