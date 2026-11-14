
from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


class Student(Person):

    def __init__(self, name, age, person_id, department, gpa):
        super().__init__(name, age, person_id)

        self.department = department
        self.__gpa = gpa
        self.__courses = []

   
    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
            print("GPA updated successfully.")
        else:
            print("Invalid GPA.")

    def enroll_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
            print(f"{self.name} enrolled in {course}.")
        else:
            print("Already enrolled in this course.")

    def get_role(self):
        return "Student"

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.person_id}")
        print(f"Department: {self.department}")
        print(f"GPA: {self.__gpa}")
        print(f"Courses: {self.__courses}")

class Teacher(Person):

    def __init__(self, name, age, person_id, subject, salary):
        super().__init__(name, age, person_id)

        self.subject = subject
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print("Salary updated successfully.")
        else:
            print("Invalid salary.")

    def get_role(self):
        return "Teacher"

    def display_info(self):
        print("\n--- Teacher Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.person_id}")
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.__salary}")

class Administrator(Person):

    def __init__(self, name, age, person_id, department, salary):
        super().__init__(name, age, person_id)

        self.department = department
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print("Administrator salary updated.")
        else:
            print("Invalid salary.")

    def get_role(self):
        return "Administrator"

    def display_info(self):
        print("\n--- Administrator Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.person_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.__salary}")


def show_person_details(person):

    print("\nRole:", person.get_role())

    person.display_info()


class University:

    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []
        self.teachers = []
        self.administrators = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully.")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print("Teacher added successfully.")

    def add_administrator(self, administrator):
        self.administrators.append(administrator)
        print("Administrator added successfully.")

    def show_all_people(self):

        all_people = (
            self.students +
            self.teachers +
            self.administrators
        )

        for person in all_people:
            show_person_details(person)

    def total_people(self):

        return (
            len(self.students) +
            len(self.teachers) +
            len(self.administrators)
        )


university = University("First Capital University")


student1 = Student(
    "Asibul",
    23,
    "ST101",
    "CSE",
    3.90
)

student2 = Student(
    "Rahim",
    22,
    "ST102",
    "EEE",
    3.65
)

teacher1 = Teacher(
    "Mr. Karim",
    40,
    "TC101",
    "Python Programming",
    65000
)

admin1 = Administrator(
    "Mr. Hasan",
    45,
    "AD101",
    "Administration",
    80000
)


# Adding people to university

university.add_student(student1)
university.add_student(student2)

university.add_teacher(teacher1)

university.add_administrator(admin1)


# Display all people

print("\n================================")
print(university.university_name)
print("================================")

university.show_all_people()


# Encapsulation demonstration

print("\n--- Encapsulation Demonstration ---")

print("Old GPA:", student1.get_gpa())

student1.set_gpa(3.95)

print("New GPA:", student1.get_gpa())


# Course enrollment

print("\n--- Course Enrollment ---")

student1.enroll_course("Python")
student1.enroll_course("Data Structures")
student1.enroll_course("Database Management")


# Total people

print("\nTotal University Members:",
      university.total_people())
