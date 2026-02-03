from HandleOperation import *

class HandleInput:
    def inputs(self):
        o = Operations()
        while True:
            print("1. Register\n2. Login")
            ch = input("Enter Your Choice ")
            if ch == "1":
                o.register()
            elif ch == "2":
                res = o.login()
                if res:
                    while True:
                        print("3. Add Customer\n4. View Plans\n5. Recharge\n6. Exit")
                        choice = input("Enter Choice ")
                        if choice == "3":
                            o.add_customers()
                        elif choice == "4":
                            o.view_plans()
                        elif choice == "5":
                            o.recharge()
                        elif choice == "6":
                            print("Exiting System...")
                            break
                        else:
                            print("Enter Valid Input....")
            elif ch == "e":
                print("Exiting System...")
                break
            else:
                print("Wrong Input....")
