def view_all_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    name = input('Add Task Name: ')
    tasks.append(name)
    print(f'Task "{name}" added.')

def delete_task(tasks):
    view_all_tasks(tasks)
    try:
        index = int(input("Enter the task number to be deleted: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f'Task "{removed}" deleted.')
        else:
            print("Invalid task number selected")
    except ValueError:
        print("Please enter a valid number.")

tasks = []
while True:
    print('\nTo-do List | Choose option')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Delete Task')
    print('4. Exit')
    choice = input('Enter your choice: ')

    match choice:
        case '1':
            view_all_tasks(tasks)
        case '2':
            add_task(tasks)
        case '3':
            delete_task(tasks)
        case '4':
            print("Exiting To-Do List. Goodbye!")
            break
        case _:
            print('Invalid choice')
