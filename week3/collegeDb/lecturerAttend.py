from database import create_connection
import sqlite3

class LecturerAttend():
    def add_lecturer_attendance(self,class_id, lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO LecturerAttend (ClassID, LecturerID) VALUES (?, ?)",
                (class_id, lecturer_id)
            )
            conn.commit()
            print("Added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


    def view_lecturer_attendance(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LecturerAttend")
        rows = cursor.fetchall()
        conn.close()
        return rows


    def delete_lecturer_attendance(self,class_id, lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM LecturerAttend WHERE ClassID = ? AND LecturerID = ?",
            (class_id, lecturer_id)
        )
        conn.commit()
        conn.close()
        print("Record deleted.")
