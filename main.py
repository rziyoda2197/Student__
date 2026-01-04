class Student:
    def __init__(self, name: str):
        self.name = name

    def calculate_grade(self):
        pass


class SchoolStudent(Student):
    def calculate_grade(self):
        return "Grade is based on exams"


class UniversityStudent(Student):
    def calculate_grade(self):
        return "Grade is based on exams and projects"


students = [
    SchoolStudent("Aziz"),
    UniversityStudent("Madina")
]

for student in students:
    print(f"{student.name}: {student.calculate_grade()}")
