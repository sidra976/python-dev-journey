import json
import os
FILE_NAME = 'notes.json'
def load_notes():
    if os.path.exists(FILE_NAME):
        with open('notes.json' , 'w') as file:
            return json.load()
        return []
    
def add_notes():
    note = input('Enter note: ')
    date = input('Enter date: ')
    notes.append({'notes' : note , 'date' : date})
    print(notes)
def view_all_notes(notes):
    pass
def delete_notes(notes):
    pass
notes = load_notes()   

while True:
    print('\nTo-do List | Choose option')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Delete Task')
    print('4. Exit')
    choice = input('Enter your choice: ')

    match choice:
        case '1':
            view_all_notes(notes)
        case '2':
            add_notes(notes)
        case '3':
            delete_notes(notes)
        case '4':
            print("Exiting To-Do List. Goodbye!")
            break
        case _:
            print('Invalid choice')

