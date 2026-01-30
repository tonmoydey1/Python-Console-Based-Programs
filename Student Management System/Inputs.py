import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="studentmanagement"
    )

# ---------------- CRUD OPERATIONS ----------------
def add_student():
    std_id = int(input("Enter Student Id"))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    conn = connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO students (std_id,name, age, course, phone, email)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (std_id,name, age, course, phone, email)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

    print("✅ Student added successfully")

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    print("\n--- Student List ---")
    for student in students:
        print(student)

def search_student():
    student_id = int(input("Enter student ID: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE std_id = %s", (student_id,))
    student = cursor.fetchone()
    conn.close()

    if student:
        print("✅ Student Found:", student)
    else:
        print("❌ Student not found")

def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")

    conn = connect_db()
    cursor = conn.cursor()
    sql = """UPDATE students
             SET name=%s, age=%s, course=%s, phone=%s, email=%s
             WHERE std_id=%s"""
    values = (name, age, course, phone, email, student_id)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

    print("✅ Student updated successfully")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE std_id=%s", (student_id,))
    conn.commit()
    conn.close()

    print("✅ Student deleted successfully")

# ---------------- MAIN MENU ----------------
def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice")

# ---------------- PROGRAM START ----------------
if __name__ == "__main__":
    main_menu()