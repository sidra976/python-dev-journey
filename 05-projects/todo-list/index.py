
def view_all_tasks(tasks):
    pass
def add_task(tasks):
    pass
def delete_task(tasks):
    pass

tasks = []
while True:
    print('\n To-do List | Choose option')
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
            break
        case _:
            print('Invalid choice')    


  
