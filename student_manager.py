# student_manager.py
# Handles MySQL CRUD operations

from database import create_connection
from models import Student

class StudentManager:

    def add_student(self, name, age, marks):
        conn = create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, marks))
        conn.commit()
        print(f"\nStudent '{name}' added successfully!")
        conn.close()

    def display_all_students(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY name ASC")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("\nNo student records found.")
            return

        print("\nList of Students (sorted by name):")
        for row in rows:
            student = Student(*row)
            print(student)

    def search_student(self, student_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            student = Student(*row)
            print("\nStudent found:")
            print(student)
        else:
            print("\nStudent not found.")

    def update_student(self, student_id, name, age, marks):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        row = cursor.fetchone()

        if not row:
            print("\nStudent not found.")
            conn.close()
            return

        sql = "UPDATE students SET name = %s, age = %s, marks = %s WHERE id = %s"
        cursor.execute(sql, (name, age, marks, student_id))
        conn.commit()
        print(f"\nStudent with ID {student_id} updated successfully!")
        conn.close()

    def delete_student(self, student_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"\nStudent with ID {student_id} deleted successfully.")
        else:
            print("\nStudent not found.")
        conn.close()
