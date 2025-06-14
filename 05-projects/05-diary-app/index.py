import json
import os

FILE_NAME = 'notes.json'

def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(FILE_NAME, 'w') as file:
        json.dump(notes, file, indent=4)

def add_notes(notes):
    note = input('Enter note: ')
    date = input('Enter date: ')
    notes.append({'note': note, 'date': date})
    save_notes(notes)  # save after adding
    print("Note added!")

def view_all_notes(notes):
    if not notes:
        print("No notes yet.")
    for i, user_notes in enumerate(notes, start=1):
        print(f"{i}. {user_notes['note']}, date: {user_notes['date']}")

# MAIN LOOP
notes = load_notes()

while True:
    print('\nTo-do List | Choose option')
    print('1. View Notes')
    print('2. Add Note')
    print('3. Exit')
    choice = input('Enter your choice: ')

    match choice:
        case '1':
            view_all_notes(notes)
        case '2':
            add_notes(notes)
        case '3':
            print("Exiting Notes App. Goodbye!")
            break
        case _:
            print('Invalid choice')
