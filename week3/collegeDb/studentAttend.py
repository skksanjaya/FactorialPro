from database import create_connection
import sqlite3

# Add Student Attendance
def add_student_attendance(student_id, class_id):
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

# View all Student Attendance
def view_student_attendance():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM StudentAttend")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Delete Student Attendance (by StudentID & ClassID)
def delete_student_attendance(student_id, class_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM StudentAttend WHERE StudentID = ? AND ClassID = ?",
        (student_id, class_id)
    )
    conn.commit()
    conn.close()
    print("Record deleted.")
