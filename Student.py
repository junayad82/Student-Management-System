students = []
while True:
    print("\n===== STUDENT MANGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update Marks")
    print("5. Delete student")
    print("6. Show top student")
    print("7. Save Data")
    print("8. Exit")
    
    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
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

        with open("students.txt", "a") as file:
            file.write(f"{student['name']} float{student['marks']} {student['grade']} ")

        print("student added successfully")

    # View student
    elif choice == "2":
        if len(students) == 0:
            print("No studets found.")
        else:
            print("\n Student List: ")
            for i, student in enumerate(students, start=1):
                print(
                    f"{i}. Name: {student['name']} | "
                    f"Marks: {student['marks']} | "
                    f"Grade: {student['grade']} "
                )
    
    # Search student
    elif choice == "3":
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
    
    # Update student

    elif choice == "4":

        search_name = input("Enter student name to update mark: ")

        found = False

        for student in students:
            if search_name.lower() == student["name"].lower():

                marks = float(input("Enter new mark: "))

                student["marks"] = marks

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

                student["grade"] = grade

                print("Student mark update successfully!")

                found = True
                break

        if not found:
            print("No student founded")
                
    # Delete student
    elif choice == "5":
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
    
    # Show top student

    elif choice == "6":
        if len(students) == 0:

            print("No student founded")

        else:
            top_students = students[0]
            for student in students:
                if student["marks"] > top_students["marks"]:
                    top_students = student
            print("\nTop student:")
            print(f"Student name:{top_students['name']}")
            print(f"Student mark: {top_students['marks']}")
            print(f"Student grade: {top_students['grade']}")

    # Save Data

    elif choice == "7":
        try:
            with open("students.txt", "r") as file:
                data = file.read()

                if data:
                    print("====File Data====")
                    print(data)
                else:
                    print("No save data")
        except FileNotFoundError:
            print("No data available")
                
    # Exit
    elif choice == "8":
        print("Exiting programe...")
        break
    else:
        print("Invalid choice.")