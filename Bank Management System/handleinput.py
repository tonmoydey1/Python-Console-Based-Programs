from handleoperations import *

class Inputs:
    def handle_inputs(self):
        lr = LoginAndRegister()
        o = Operations()
        while True:
            print("Welcome to Bank Management System")
            print("*" * 30)
            print("1. Register\n2. Login\n3. Exit")

            ch = input("Enter Choice ")

            if ch == "1":
                lr.register()
            elif ch == "2":
                res = lr.login()
                if res:
                    while True:
                        print(
                            "3. Create Account\n4. Deposit Money\n5. Withdraw Money\n6. Check Balance\n7. Close Account\n8. Exit")
                        choice = input("Enter Choice ")
                        if choice == "3":
                            o.create_account()
                        elif choice == "4":
                            o.deposit_money()
                        elif choice == "5":
                            o.withdraw_money()
                        elif choice == "6":
                            o.check_balance()
                        elif choice == "7":
                            o.close_account()
                        elif choice == "e" or choice == "E":
                            print("Exiting System....")
                            break
                        else:
                            print("Wrong Choice....")
            elif ch == "3":
                print("Exiting System....")
                break

            else:
                print("Wrong Choice....")



