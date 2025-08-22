from database import create_connection
import sqlite3

class Subject():
    def add_subject(self,subject_name, description, class_id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Subject (SubjectName, Description, ClassID) VALUES (?, ?, ?)",
                (subject_name, description, class_id)
            )
            conn.commit()
            print("Added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

    # View all Subjects
    def view_subjects(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Subject")
        rows = cursor.fetchall()
        conn.close()
        return rows

    # Delete Subject by ID
    def delete_subject(self,subject_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Subject WHERE SubjectID = ?", (subject_id,))
        conn.commit()
        conn.close()
        print("Record deleted.")
