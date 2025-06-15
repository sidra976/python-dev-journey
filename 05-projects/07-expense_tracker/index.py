import json
import os
FILE_NAME = 'expense_manager.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        return[]

def save_tasks(expenses):
     with open(FILE_NAME, 'w') as file:
         json.dump(expenses, file)

def view_total_expense(expenses):
    for index, user_expense in enumerate(expenses, start=1):
        pass

def add_expense(expenses):
    expense_name = input('Add expense name: ')
    date = input('Add date: ')
    expenses.append({'Expense name' : expense_name , 'Date' : date})
    save_tasks(expenses)

def delete_expense(expenses):
    pass

def main():
    expenses = load_tasks()
    while True:
        print('\nExpense Tracker App')
        print('1. View total expense')
        print('2. Add Expense')
        print('3. Delete Expense')
        print('4. Exit')
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                view_total_expense(expenses)
            case '2':
                add_expense(expenses)
            case '3':
                delete_expense(expenses)
            case '4':
                print("Exiting. Goodbye!")
                break
            case _:
                print('Invalid choice')

if __name__ == '__main__':
    main()
