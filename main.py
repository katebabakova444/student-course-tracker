from datetime import datetime

courses = {}

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    @property
    def is_passing(self):
        return self.average() >= 60

    def __str__(self):
        return f"{self.name} - average: {self.average():.1f}"


class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def passed_students(self):
        return [student for student in self.students if student.is_passing]

    def __str__(self):
        return f"{self.title} - {len(self.students)} students"


def get_course_by_name():
    course_name = input("Enter course name: ")
    if course_name in courses:
        return courses[course_name]
    print("Error: course not found.")
    return None


def add_student_to_course():
    course = get_course_by_name()
    if not course:
        return
    name = input("Enter student name: ")
    student = Student(name)
    course.add_student(student)
    print(f"Student '{name}' added to '{course.title}'")


def add_grade_to_student():
    course = get_course_by_name()
    if not course:
        return

    print(f"Students in {course.title}:")
    for student in course.students:
        print("-", student.name)

    name = input("Enter student name: ")
    target = None
    for student in course.students:
        if student.name == name:
            target = student
            break

    if target:
        grade = int(input("Enter student grade: "))
        target.add_grade(grade)
        print("Grade added.")
    else:
        print("Student not found.")


def show_all_students():
    course = get_course_by_name()
    if not course:
        return
    print(f"Students in {course.title}:")
    for student in course.students:
        print(f"{student.name}: {student.average():.1f}")


def show_passed_students():
    course = get_course_by_name()
    if not course:
        return
    passed = course.passed_students()
    if passed:
        print("Students who passed:")
        for student in passed:
            print(student.name)
    else:
        print("No students passed.")


def save_data_to_file():
    with open("courses_report.txt", "w") as file:
        if not courses:
            file.write("No courses available.\n")
            return
        for course in courses.values():
            file.write(f"Course: {course.title}\n")
            if not course.students:
                file.write("  No students enrolled.\n\n")
                continue
            for student in course.students:
                status = "PASSED" if student.is_passing else "FAILED"
                file.write(f"  - {student.name}: {student.average():.1f} ({status})\n")
            file.write("\n")
    print("Data saved to courses_report.txt")


# ========== Main Menu ==========
while True:
    print("\nMenu:")
    print("[1] Create a course")
    print("[2] Add student to course")
    print("[3] Add grade to student")
    print("[4] Show all students in course")
    print("[5] Show passed students")
    print("[6] Save report to file")
    print("[0] Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter course title: ")
        if title in courses:
            print("This course already exists.")
        else:
            course = Course(title)
            courses[title] = course
            print(f"Course '{title}' created.")

    elif choice == "2":
        add_student_to_course()

    elif choice == "3":
        add_grade_to_student()

    elif choice == "4":
        show_all_students()

    elif choice == "5":
        show_passed_students()

    elif choice == "6":
        save_data_to_file()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")