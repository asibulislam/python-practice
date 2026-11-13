from datetime import date


class Person:
    """Base class for everyone in the school."""

    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def describe(self):
        return f"{self.__class__.__name__} #{self.person_id}: {self.name}"


class Teacher(Person):
    def __init__(self, person_id, name, subject):
        super().__init__(person_id, name)
        self.subject = subject

    def describe(self):
        return f"{super().describe()} (teaches {self.subject})"


class Student(Person):
    def __init__(self, person_id, name, grade):
        super().__init__(person_id, name)
        self.grade = grade
        self.attendance = {}  # {date: True/False}

    def mark_attendance(self, day, present):
        self.attendance[day] = present

    def attendance_rate(self):
        if not self.attendance:
            return 0.0
        present_days = sum(self.attendance.values())
        return present_days / len(self.attendance) * 100

    def describe(self):
        return f"{super().describe()} | Grade {self.grade}"


class SchoolClass:
    """A class (section) made up of one teacher and many students."""

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def take_attendance(self, present_ids, day=None):
        day = day or date.today()
        for student in self.students:
            student.mark_attendance(day, student.person_id in present_ids)
        print(f"Attendance recorded for {self.name} on {day}")

    def report(self):
        print(f"\nClass: {self.name} | Teacher: {self.teacher.name}")
        for student in self.students:
            print(f"  {student.name:<15} {student.attendance_rate():6.2f}% present")


if __name__ == "__main__":
    teacher = Teacher(1, "Mr. Rahman", "Mathematics")
    class_a = SchoolClass("10-A", teacher)

    class_a.add_student(Student(101, "Alif", 10))
    class_a.add_student(Student(102, "Nadia", 10))
    class_a.add_student(Student(103, "Imran", 10))

    print(teacher.describe())
    print(class_a.students[0].describe())

    class_a.take_attendance(present_ids={101, 103}, day=date(2026, 11, 9))
    class_a.take_attendance(present_ids={101, 102}, day=date(2026, 11, 10))
    class_a.take_attendance(present_ids={101}, day=date(2026, 11, 11))

    class_a.report()