from handleOperation import *

def handleInput():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add employee")
        print("2. View  employee")
        print("3. Search employee")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Exit")

        choice = input("Enter Choice ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employee()
        elif choice == "3":
            srch_employee()
        elif choice == "4":
            upd_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice")