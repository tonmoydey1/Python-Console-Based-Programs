from handleOperation import *

def handle_inp():
    while True:
        print("\n---------Welcome To Library Management System-------------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        ch = input("Enter Choice ")

        if ch == "1":
            add_patient()
        elif ch == "2":
            pass
        elif ch == "3":
            pass
        elif ch == "4":
            pass
        elif ch == "5":
            pass
        elif ch == "6":
            print("Exiting System......")
            break
        else:
            print("Wrong Choice ")