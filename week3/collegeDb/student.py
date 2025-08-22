from database import create_connection
import sqlite3

class StudentData():
    def add_student(self,name, dob, email, phone):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Student (Name, DOB, Email, Phone) VALUES (?, ?, ?, ?)",
                (name, dob, email, phone)
            )
            conn.commit()
            print("Added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


    def view_students(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student")
        rows = cursor.fetchall()
        conn.close()
        return rows


    def delete_student(self,student_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Student WHERE StudentID = ?", (student_id,))
        conn.commit()
        conn.close()
        print("Student deleted.")