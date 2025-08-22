from database import create_connection
import sqlite3


def add_lecturer(name, dob, email, phone, subject_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Lecturer (Name, DOB, Email, Phone, SubjectID) VALUES (?, ?, ?, ?, ?)",
            (name, dob, email, phone, subject_id)
        )
        conn.commit()
        print("Added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Lecturer")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_lecturer(lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Lecturer WHERE LecturerID = ?", (lecturer_id,))
    conn.commit()
    conn.close()
    print("Record deleted.")
