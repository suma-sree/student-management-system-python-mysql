# models.py
# Student model object

class Student:
    """
    Student object representing one student record.
    """

    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}"
