import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
   
   # Create Student table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100) NOT NULL,
            DOB DATE,
            Email VARCHAR(100) UNIQUE,
            Phone VARCHAR(20)
        )
    ''')

    # Create Class table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Class (
            ClassID INTEGER PRIMARY KEY AUTOINCREMENT,
            ClassName VARCHAR(100) NOT NULL,
            Description VARCHAR(255)
        )
    ''')

    # Create StudentAttend table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS StudentAttend (
            StudentID INTEGER,
            ClassID INTEGER,
            FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
            FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
        )
    ''')

    # Create Subject table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subject (
            SubjectID INTEGER PRIMARY KEY AUTOINCREMENT,
            SubjectName VARCHAR(100) NOT NULL,
            Description VARCHAR(255),
            ClassID INTEGER,
            FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
        )
    ''')

    # Create Lecturer table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturer (
            LecturerID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100) NOT NULL,
            DOB DATE,
            Email VARCHAR(100) UNIQUE,
            Phone VARCHAR(20),
            SubjectID INTEGER,
            FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
        )
    ''')

    # Create LecturerAttend table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LecturerAttend (
            ClassID INTEGER,
            LecturerID INTEGER,
            FOREIGN KEY (ClassID) REFERENCES Class(ClassID),
            FOREIGN KEY (LecturerID) REFERENCES Lecturer(LecturerID)
        )
    ''')


    
    conn.commit()
    conn.close()
