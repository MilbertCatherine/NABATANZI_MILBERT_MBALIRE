# Base class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Student subclass
class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

# Lecturer subclass
class Lecturer(Person):
    def __init__(self, name, age, gender, staff_id, department):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Staff ID (Lecturer): {self.staff_id}")
        print(f"Department: {self.department}")

# Staff subclass
class Staff(Person):
    def __init__(self, name, age, gender, staff_id, position):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Staff ID (Staff): {self.staff_id}")
        print(f"Position: {self.position}")

# === Sample Usage ===

print("=== Student Information ===")
student = Student("Alice", 20, "Female", "S12345", "Computer Science")
student.display_info()

print("\n=== Lecturer Information ===")
lecturer = Lecturer("Dr. John", 45, "Male", "L67890", "Engineering")
lecturer.display_info()

print("\n=== Staff Information ===")
staff = Staff("Ms. Grace", 35, "Female", "ST54321", "Registrar")
staff.display_info()
