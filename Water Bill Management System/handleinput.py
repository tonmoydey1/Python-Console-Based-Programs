from handleoperation import *

class HandleInput:
    def inputs(self):
        o = Operations()
        while True:
            print("Welcome To Water Bill Management")
            print("*" * 30)
            print("1. Add Consumer\n2. Enter Usage Units\n3. Generate Bill\n4. Pay Bill\n5. View Payments\n6. Exit")

            ch = input("Enter Your Choice ")

            if ch == "1":
                o.add_consumer()
            elif ch == "2":
                o.add_usage()
            elif ch == "3":
                o.generate_bill()
            elif ch == "4":
                o.pay_bill()
            elif ch == "5":
                o.view_payments()
            elif ch == "6":
                print("Exiting System...........")
                break
            else:
                print("Wrong Input.......")
