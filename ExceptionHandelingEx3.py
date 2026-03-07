# Student Management System with Exception Handling

students = []

def add_student():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        student = {
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)

    except ValueError:
        print("Error: Age must be integer and marks must be number!")

    else:
        print("Student added successfully!")

    finally:
        print("Add student operation completed.\n")


def display_students():
    try:
        if len(students) == 0:
            raise Exception("No students found")

        for i, s in enumerate(students):
            print(f"{i+1}. Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")

    except Exception as e:
        print("Error:", e)

    finally:
        print("Display operation finished.\n")


def search_student():
    try:
        name = input("Enter student name to search: ")
        found = False

        for s in students:
            if s["name"].lower() == name.lower():
                print("Student Found:")
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Marks:", s["marks"])
                found = True
                break

        if not found:
            raise Exception("Student not found")

    except Exception as e:
        print("Error:", e)

    finally:
        print("Search operation completed.\n")


while True:
    try:
        print("------ Student Management System ------")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")

    finally:
        print("Main menu operation completed.\n")