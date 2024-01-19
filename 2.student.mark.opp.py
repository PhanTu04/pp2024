class Student:
    def __init__(self, student_id, student_name, date_of_birth):
        self.student_id = student_id
        self.student_name = student_name
        self.date_of_birth = date_of_birth

    def input_student_info(self):
        self.student_name = input("Name: ")
        self.student_id = input("Student ID: ")
        self.date_of_birth = input("Date of birth (example: dd/mm/yyyy): ")

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.student_name}, Date of Birth: {self.date_of_birth}"


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def input_course_info(self):
        self.course_name = input("Name of the course: ")
        self.course_id = input("Course ID: ")

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.course_name}"


class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    def input_marks(self):
        self.student_id = input("Student ID: ")
        self.course_id = input("Course ID: ")
        self.mark = float(input("Mark: "))

    def __str__(self):
        return f"Student ID: {self.student_id}, Course ID: {self.course_id}, Mark: {self.mark}"


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_info(self):
        student = Student("", "", "")
        student.input_student_info()
        self.students.append(student)

    def input_course_info(self):
        course = Course("", "")
        course.input_course_info()
        self.courses.append(course)

    def input_marks(self):
        mark = Mark("", "", 0)
        mark.input_marks()
        self.marks.append(mark)

    def list_students(self):
        for student in self.students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)

    def list_marks(self):
        for mark in self.marks:
            print(mark)


def main():
    school_system = SchoolManagementSystem()

    while True:
        print("1. Input student info")
        print("2. Input course info")
        print("3. Input mark")
        print("4. List students")
        print("5. List courses")
        print("6. List marks")
        print("7. Exit")

        option = int(input("Select an option: "))

        if option == 1:
            school_system.input_student_info()
        elif option == 2:
            school_system.input_course_info()
        elif option == 3:
            school_system.input_marks()
        elif option == 4:
            school_system.list_students()
        elif option == 5:
            school_system.list_courses()
        elif option == 6:
            school_system.list_marks()
        elif option == 7:
            break
        else:
            print("No valid option. Try again.")


if __name__ == "__main__":
    main()
