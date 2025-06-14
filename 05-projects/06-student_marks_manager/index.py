import json
import os

FILE_NAME = 'student_marks_manager.json'

def load_student_marks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        return[]
def save_student_marks(student_marks):
    with open(FILE_NAME, 'w') as file:
        json.dump(student_marks, file)

def view_all_student_marks(student_marks):
    if not student_marks:
        print('No student marks available')
    else:
     for i, student in enumerate(student_marks, start=1):
        print(f"{i}, {student['name']} Marks: {student['marks']}")

def add_student(student_marks):

    name = input('Enter student name: ')
    marks = input('Enter marks: ')

    student_marks.append({'name' : name, 'marks' : marks})
    save_student_marks(student_marks)
    print('Student Marks Added!')

def update_marks(student_marks):
    view_all_student_marks(student_marks)
    i = int(input('Enter the student no to update the marks: '))
    if 1 <= i <= len(student_marks):
        marks = input('Enter marks: ')
        student_marks[i-1]['marks'] = marks  
        save_student_marks(student_marks)
    else:
        print("Invalid index selected")


student_marks = load_student_marks()
while True:
    print('\nStudent Marks Manager Site')
    print('1. View All Student Marks')
    print('2. Add New Student')
    print('3. Update Marks')
    print('4. Exit')
    choice = input('Enter your choice: ')

    match choice:
        case '1':
            view_all_student_marks(student_marks)
        case '2':
            add_student(student_marks)
        case '3':
            update_marks(student_marks)    
        case '4':
            print("Exiting Student Manager. Goodbye!")
            break
        case _:
            print('Invalid choice')
