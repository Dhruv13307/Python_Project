import sqlite3

def get_connection():
    return sqlite3.connect("students.db")


def add_student(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?)",
        data
    )
    conn.commit()
    conn.close()


def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_student(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students SET
        name=?, class=?, section=?, contact=?, father=?, address=?, gender=?, dob=?
        WHERE roll=?
    """, data)
    conn.commit()
    conn.close()


def delete_student(roll):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
    conn.commit()
    conn.close()


def search_students(field, value):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM students WHERE {field} LIKE ?"
    cursor.execute(query, ('%' + value + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows
