from database import create_connection
import sqlite3

class SysUser():
    def add_user(self,Name, Address,Email,RoleID,PasswordHash,Phone):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Class (Name, Address,Email,RoleID,PasswordHash,Phone) VALUES (?, ?,?, ?,?, ?)",
                (Name, Address,Email,RoleID,PasswordHash,Phone)
            )
            conn.commit()
            print("Class added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def check_user_exists(self, Email):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT 1 FROM SysUser WHERE Email = ?", (Email,))
            if cursor.fetchone():
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()