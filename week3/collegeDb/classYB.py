from database import create_connection
import sqlite3

# Add Class record
def add_class(class_name, description):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Class (ClassName, Description) VALUES (?, ?)",
            (class_name, description)
        )
        conn.commit()
        print("✅ Class added successfully.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        conn.close()

# View all Classes
def view_classes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Class")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Delete Class by ID
def delete_class(class_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Class WHERE ClassID = ?", (class_id,))
    conn.commit()
    conn.close()
    print("🗑️ Class deleted.")
