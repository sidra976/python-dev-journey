import sqlite3

# ---------- DB Setup ----------
def load_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

# ---------- Save Not Needed (DB auto saves) ----------
def save_tasks():
    # Using SQLite, so no need for manual save
    pass

# ---------- View ----------
def view_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("📭 No tasks found.")
    else:
        for t in tasks:
            print(f"{t[0]}. {t[1]}")

# ---------- Add ----------
def add_task():
    title = input("Enter task title: ")
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    print("✅ Task added.")

# ---------- Delete ----------
def delete_task():
    task_id = input("Enter task ID to delete: ")
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print("🗑️ Task deleted.")

# ---------- Main ----------
def main():
    load_tasks()  # Ensure table is created
    while True:
        print('\n📝 To-Do List')
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
                print('⚠️ Invalid choice')

# ---------- Run ----------
if __name__ == '__main__':
    main()
