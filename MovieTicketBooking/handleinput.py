from handleoperation import *

class Input:
    def handle_input(self):
        o = Operations()
        while True:
            print("Welcome To Movie Management System..........")
            print("1. Register\n2. Login\nE. Exit")

            ch = input("Enter Choice ")

            if ch == "1":
                o.register()
            elif ch == "2":
                res = o.login()
                if res is not None:
                    while True:
                        print("3. Add Movie\n4. View Movie\n5. Book Ticket\nE. Exit")

                        choice = input("Enter Choice ")

                        if choice == "3":
                            o.add_movies()
                        elif choice == "4":
                            o.view_movies()
                        elif choice == "5":
                            o.book_ticket()
                        elif choice == "E" or choice == "e":
                            print("Exiting System.....")
                            break
            elif ch == "E" or ch == "e":
                print("Exiting System.....")
                break