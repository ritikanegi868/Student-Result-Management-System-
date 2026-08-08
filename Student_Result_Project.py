# Student Result Management System


students = {}


def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    math = float(input("Enter Mathematics marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))

    students[roll_no] = {
        "name": name,
        "math": math,
        "science": science,
        "english": english
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n===== Student Records =====")

    for roll_no, data in students.items():
        total = data["math"] + data["science"] + data["english"]
        average = total / 3

        print("\nRoll Number:", roll_no)
        print("Name:", data["name"])
        print("Mathematics:", data["math"])
        print("Science:", data["science"])
        print("English:", data["english"])
        print("Total:", total)
        print("Average:", round(average, 2))


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no not in students:
        print("Student not found!")
        return

    data = students[roll_no]
    total = data["math"] + data["science"] + data["english"]
    average = total / 3

    print("\n===== Student Details =====")
    print("Roll Number:", roll_no)
    print("Name:", data["name"])
    print("Mathematics:", data["math"])
    print("Science:", data["science"])
    print("English:", data["english"])
    print("Total:", total)
    print("Average:", round(average, 2))


def update_marks():
    roll_no = input("Enter Roll Number: ")

    if roll_no not in students:
        print("Student not found!")
        return

    print("Enter new marks:")
    students[roll_no]["math"] = float(input("Mathematics: "))
    students[roll_no]["science"] = float(input("Science: "))
    students[roll_no]["english"] = float(input("English: "))

    print("Marks updated successfully!")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def main():
    while True:
        print("\n====================================")
        print("   STUDENT RESULT MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()