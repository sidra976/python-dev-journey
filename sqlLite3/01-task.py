import sqlite3

def load_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute(""" 
     CREATE TABLE IF NOT EXISTS notes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          title TEXT NOT NULL               
     )
""")
    conn.commit()
    return conn

def view_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title FROM notes')
    notes = cursor.fetchall()
    conn.close()

    if not notes:
        print('No notes available')
    else:
        for note in notes:
            print(f"{note[0]}. {note[1]}")


def add_note():
    title = input('Enter note: ')
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()
    print('Note Added!')

def delete_note():
    view_notes()
    note_id = input("Enter note ID to delete: ")
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    print("Note deleted!")

def main():
      load_notes()
      while True:
        print('\n Notes App')
        print('1. View Notes')
        print('2. Add Notes')
        print('3. Delete Note')
        print('4. Exit')
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                view_notes()
            case '2':
                add_note()
            case '3':
                delete_note()
            case '4':
                print("Exiting. Goodbye!")
                break
            case _:
                print('Invalid choice')


if __name__ == '__main__':
    main()
