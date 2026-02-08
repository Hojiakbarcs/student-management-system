# Student Management System
# Author: Hojiakbar Akramov

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    students.append({"name": name, "age": age})
    print("Student added successfully.")

def view_students():
    if not students:
        print("No students found.")
        return
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} - Age: {student['age']}")

def remove_student():
    view_students()
    if not students:
        return
    index = int(input("Enter student number to remove: "))
    if 1 <= index <= len(students):
        students.pop(index - 1)
        print("Student removed.")
    else:
        print("Invalid number.")

while True:
    print("\nStudent Management System")
    print("1) Add student")
    print("2) View students")
    print("3) Remove student")
    print("4) Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
