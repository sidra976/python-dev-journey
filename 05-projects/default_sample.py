def view_tasks():
    pass

def add_task():
    pass

def delete_task():
    pass

def main():
    pass

def save_tasks():
    pass

def load_tasks():
    pass

tasks = load_tasks()
while True:
    print('\nTo-Do List')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Delete Task')
    print('4. Exit')
    choice = input('Enter your choice: ')
    match choice:
        case '1':
            view_tasks()
        case '2':
            add_task()
        case '3':
            delete_task()
        case '4':
            print("Exiting. Goodbye!")
            break
        case _:
            print('Invalid choice')
