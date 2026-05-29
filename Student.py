students = []
while True:
    print("\n===== STUDENT MANGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    # Add student
    if choice == 1:
        name = input("Enter student name: ")
        marks = float(input("Enter studens marks: "))
        # Grade system
        if marks >= 80:
            grade = "A+"
        elif marks >= 70:
            grade = "A"
        elif marks >= 60:
            grade = "A-"
        elif marks >= 50:
            grade = "B"
        else:
            grade = "F"
        student = {
            "name": name,
            "marks": marks,
            "grade": grade
        }
        students.append(student)
        print("student added successfully")

    # View student
    elif choice == 2:
        if len(students) == 0:
            print("No studets found.")
        else:
            print("\n Student List: ")
            for i, students in enumerate(students, start=1):
                print(
                    f"{i}. Name: {student['name']} | "
                    f"Marks: {student['marks']} | "
                    f"Grade: {student['grade']} "
                )
    
    # Search student
    elif choice == 3:
        search_name = input("Enter student name to search: ")
        found = False

        for student in students:
            if search_name.lower() == student["name"].lower():
                print("\nStudent Found:")
                print(f"Name:{student['name']}")
                print(f"Marks: {student['marks']}")
                print(f"Grade: {student['grade']}")
                found = True
                break
            if not found:
                print("Student not found")
    
    # Delete student
    elif choice == 4:
        delete_name = input("Enter student name to delete: ")
        found = False
        for student in students:
            if delete_name.lower() == student["name"].lower():
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break
            if not found:
                print("Stdent not found.")

    # Exit
    elif choice == 5:
        print("Exiting programe...")
        break
    else:
        print("Invalid choice. Pleas try again.")