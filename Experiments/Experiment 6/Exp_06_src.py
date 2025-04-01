

import sqlite3

# Connect to a database (or create it if it doesn't exist)
connection = sqlite3.connect('genericDatabase.db')  # No need for './' in Google Colab
cursor = connection.cursor()

# Create Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

connection.commit()

# Create (Insertion)
def create_student(name, age):
    cursor.execute('''
        INSERT INTO students (name, age) 
        VALUES (?, ?)
    ''', (name, age))
    connection.commit()
    print("Record added successfully!")

create_student("Griffith", 20)
create_student("Guts", 22)

# Read (Retrieve)
def read_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    print("Student Records:")
    for row in rows:
        print(row)

read_students()

# Update
def update_student_age(student_id, new_age):
    cursor.execute('''
        UPDATE students 
        SET age = ? 
        WHERE id = ?
    ''', (new_age, student_id))
    connection.commit()
    print("Student age updated successfully!")

update_student_age(1, 21)  # Updating Griffith's age to 21
read_students()

# Delete
def delete_student(student_id):
    cursor.execute('''
        DELETE FROM students 
        WHERE id = ?
    ''', (student_id,))
    connection.commit()
    print("Student deleted successfully!")

delete_student(2)  # Deleting Guts' record
read_students()

# Closing the database connection
connection.close()

