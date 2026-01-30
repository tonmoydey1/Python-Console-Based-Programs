import mysql.connector as conn

class DBConnection:
    def connect(self):
        return conn.connect(host="localhost", user="root", password="12345", database="bank_db")
    def cursors(self):
        db = self.connect()
        cursor = db.cursor()
        return cursor,db

class LoginAndRegister(DBConnection):
    def register(self):
        username = input("Enter Username ")
        password = input("Enter Password ")
        cur,db = super().cursors()
        cur.execute("select username from users where username = %s",(username,))
        res = cur.fetchone()
        if res is not None:
            print("Already Registered....")
        else:
            query = "insert into users(username,password) values(%s,%s)"
            data = (username,password)
            cur.execute(query,data)
            db.commit()
            print("Registered Successfully....")
        db.close()

    def login(self):
        username = input("Enter Username ")
        password = input("Enter Password ")
        cur, db = super().cursors()
        cur.execute("select username from users where username = %s and password = %s",(username,password))
        res = cur.fetchone()
        if res:
            print(f"Welcome {res[0]}")
            return res[0]
        else:
            print("Invalid username and password.....")
            return None
        db.close()

class Operations(DBConnection):
    def create_account(self):
        cus_name = input("Enter Customer Name ")
        acc_type = input("Enter Account Type ")
        bal = int(input("Enter Balance "))
        acc_status = input("Enter Account Status ")
        cur, db = super().cursors()
        query = "insert into accounts(customer_name, account_type, balance, status) values (%s,%s,%s,%s)"
        data = (cus_name,acc_type,bal,acc_status)
        cur.execute(query,data)
        db.commit()
        cur.execute("select account_no from accounts where customer_name = %s",(cus_name,))
        res = cur.fetchone()
        print("Account created successfully and your account number is ",res[0])
        db.close()

    def deposit_money(self):
        acc_no = int(input("Enter Account Number "))
        tranc_type = input("Transaction Type ")
        deposit_amt = int(input("Enter Amount To Deposit "))
        date = input("Enter Transaction Date ")

        cur, db = super().cursors()
        cur.execute("select account_no from accounts where account_no = %s",(acc_no,))
        res = cur.fetchone()
        if res is None:
            print("No Account Found....")
        else:
            account_no = res[0]
            cur.execute("insert into transactions(account_no, transaction_type, amount, transaction_date) values(%s,%s,%s,%s)",
                        (account_no,tranc_type,deposit_amt,date))
            print(f"Amount {deposit_amt} Deposited Successfully....")
            cur.execute("update accounts set balance = balance + %s where account_no = %s",(deposit_amt,account_no))
            db.commit()
            db.close()

    def withdraw_money(self):
        acc_no = int(input("Enter Account Number "))
        tranc_type = input("Transaction Type ")
        withdraw_amt = int(input("Enter Amount To Withdraw "))
        date = input("Enter Transaction Date ")
        cur, db = super().cursors()
        cur.execute("select balance,account_no from accounts where account_no = %s",(acc_no,))
        res = cur.fetchone()
        account_no = res[1]
        if withdraw_amt > res[0]:
            print("Insufficient Balance....")
        else:
            cur.execute(
                "insert into transactions(account_no, transaction_type, amount, transaction_date) values(%s,%s,%s,%s)",
                (account_no, tranc_type, withdraw_amt, date))
            print(f"Amount {withdraw_amt} Withdraw Successfully....")
            cur.execute("update accounts set balance = balance - %s where account_no = %s", (withdraw_amt, account_no))
            db.commit()
            db.close()

    def check_balance(self):
        acc_no = int(input("Enter Account Number "))
        cur, db = super().cursors()
        cur.execute("select balance from accounts where account_no = %s",(acc_no,))
        res = cur.fetchone()
        print(res)
        if res:
            for i in res:
                print(f"Your Balance is Rs.{i}")
        else:
            print("No account found")

        db.close()

    def closing(self):
        acc_no = int(input("Enter Account Number "))
        cur, db = super().cursors()
        cur.execute("delete from accounts where account_no = %s", (acc_no,))
        print("Account Closed Successfully....")
        db.close()

    def close_account(self):
        print("Enter Closing Reason.......")
        print("1. Opened Another Account\n2. Got Better Bank\n3. Other")
        ch = input("Enter Your Choice ")
        if ch == "1":
            self.closing()
        elif ch =="2":
            self.closing()
        elif ch == "3":
            res = input("Enter Other Reason")
            if res is not None:
                self.closing()
            else:
                print("Please Enter Valid Reason")
        else:
            print("Wrong Choice...Try Again...")












