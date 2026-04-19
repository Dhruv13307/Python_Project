import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll TEXT PRIMARY KEY,
            name TEXT,
            class TEXT,
            section TEXT,
            contact TEXT,
            father TEXT,
            address TEXT,
            gender TEXT,
            dob TEXT
        )
    """)
    conn.commit()
    conn.close()
