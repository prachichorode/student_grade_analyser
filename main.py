# ==========================================
# STUDENT GRADE ANALYZER USING PYTHON
# ==========================================

students = []


# Function to calculate grade
def calculate_grade(average):

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


# Function to calculate student performance
def analyze_student(name, roll_no, marks):

    total = sum(marks.values())

    average = total / len(marks)

    # Check pass or fail
    if all(mark >= 35 for mark in marks.values()):
        status = "PASS"
    else:
        status = "FAIL"

    grade = calculate_grade(average)

    # Store student information in dictionary
    student = {
        "Name": name,
        "Roll Number": roll_no,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade,
        "Status": status
    }

    return student


# Function to display student report
def display_report(student):

    print("\n" + "=" * 45)
    print("          STUDENT PERFORMANCE REPORT")
    print("=" * 45)

    print("Student Name :", student["Name"])
    print("Roll Number  :", student["Roll Number"])

    print("\nSubject-wise Marks:")

    for subject, mark in student["Marks"].items():
        print(subject, ":", mark)

    print("\nTotal Marks  :", student["Total"])
    print("Average      :", round(student["Average"], 2), "%")
    print("Grade        :", student["Grade"])
    print("Result       :", student["Status"])

    print("=" * 45)


# Function to add student
def add_student():

    print("\n--- Enter Student Details ---")

    name = input("Enter Student Name: ")

    roll_no = input("Enter Roll Number: ")

    subjects = ["Python", "DBMS", "Mathematics", "English", "Statistics"]

    marks = {}

    for subject in subjects:

        while True:

            try:
                mark = float(input(f"Enter {subject} Marks (0-100): "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Invalid input! Enter numeric marks.")

    student = analyze_student(name, roll_no, marks)

    students.append(student)

    display_report(student)

    print("\nStudent record added successfully!")


# Function to display all students
def display_all_students():

    if not students:
        print("\nNo student records available.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:

        print("\nName:", student["Name"])
        print("Roll Number:", student["Roll Number"])
        print("Total:", student["Total"])
        print("Average:", round(student["Average"], 2))
        print("Grade:", student["Grade"])
        print("Status:", student["Status"])


# Function to display class statistics
def class_statistics():

    if not students:
        print("\nNo student records available.")
        return

    averages = [student["Average"] for student in students]

    highest = max(averages)
    lowest = min(averages)
    class_average = sum(averages) / len(averages)

    passed = sum(1 for student in students
                 if student["Status"] == "PASS")

    failed = len(students) - passed

    print("\n========== CLASS STATISTICS ==========")

    print("Total Students :", len(students))
    print("Class Average  :", round(class_average, 2))
    print("Highest Average:", round(highest, 2))
    print("Lowest Average :", round(lowest, 2))
    print("Passed Students:", passed)
    print("Failed Students:", failed)


# Main Menu
def main():

    while True:

        print("\n====================================")
        print("       STUDENT GRADE ANALYZER")
        print("====================================")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Class Statistics")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":

            add_student()

        elif choice == "2":

            display_all_students()

        elif choice == "3":

            class_statistics()

        elif choice == "4":

            print("\nThank you for using Student Grade Analyzer!")
            break

        else:

            print("\nInvalid choice! Please select 1-4.")


# Program execution
if __name__ == "__main__":
    main()
