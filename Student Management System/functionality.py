from db_connection import connect as conn

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    db = conn()
    