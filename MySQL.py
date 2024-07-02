import mysql.connector
from mysql.connector import errorcode

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kumar@2501",
        database="demo"
    )

# Create database and table
def create_database_and_table(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS demo")
    cursor.execute("USE demo")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            age INT,
            grade FLOAT
        )
    """)

# Insert a new student record
def insert_student(cursor):
    sql = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    values = ("Alice", "Smith", 18, 95.5)
    cursor.execute(sql, values)

# Update the grade of the student with first name "Alice"
def update_student_grade(cursor):
    sql = "UPDATE students SET grade = %s WHERE first_name = %s"
    values = (97.0, "Alice")
    cursor.execute(sql, values)

# Delete the student with the last name "Smith"
def delete_student(cursor):
    sql = "DELETE FROM students WHERE last_name = %s"
    values = ("Smith",)
    cursor.execute(sql, values)

# Fetch and display all student records
def fetch_all_students(cursor):
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for row in result:
        print(row)

def main():
    conn = None
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        
        create_database_and_table(cursor)
        insert_student(cursor)
        conn.commit()  # Commit the transaction

        fetch_all_students(cursor)
        # update_student_grade(cursor)
        # conn.commit()  # Commit the transaction

        # delete_student(cursor)
        # conn.commit()  # Commit the transaction
        # fetch_all_students(cursor)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()