from database import create_connection
import sqlite3

class StudentAttend():
    def add_student_attendance(self,student_id, class_id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO StudentAttend (StudentID, ClassID) VALUES (?, ?)",
                (student_id, class_id)
            )
            conn.commit()
            print("Attendance added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


    def view_student_attendance(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM StudentAttend")
        rows = cursor.fetchall()
        conn.close()
        return rows


    def delete_student_attendance(self,student_id, class_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM StudentAttend WHERE StudentID = ? AND ClassID = ?",
            (student_id, class_id)
        )
        conn.commit()
        conn.close()
        print("Record deleted.")
