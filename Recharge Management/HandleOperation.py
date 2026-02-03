import mysql.connector as conn

class DBConnection:
    def connect(self):
        return conn.connect(host="localhost",user="root",password="12345",database="recharge_db")
    def cursors(self):
        db = self.connect()
        cur = db.cursor()
        return cur,db

class Operations(DBConnection):
    def register(self):
        username = input("Enter Username ")
        password = input("Enter Password ")
        cur, db = super().cursors()
        if len(password) < 5:
            print("Username should be atleast 5 characters")
        else:
            cur.execute("select username from user where username = %s and password = %s", (username, password))
            res = cur.fetchone()
            if res is not None:
                print("Already Registered")
            else:
                cur.execute("insert into user(username,password) values(%s,%s)", (username, password))
                db.commit()
                print("Registered Succesfully.....")
                db.close()

    def login(self):
        username = input("Enter Username ")
        password = input("Enter Password ")
        cur, db = super().cursors()
        cur.execute("select username from user where username = %s and password = %s", (username, password))
        res = cur.fetchone()
        if res:
            for i in res:
                print(f"Welcome {i}")
                return res[0]
        else:
            print("Username not found..Please Register....")
            return None
        db.close()


    def add_customers(self):
        name = input("Enter Customer Name ")
        mb_no = input("Enter Mobile Number ")
        operator = input("Enter Operator ")
        cur,db = super().cursors()
        query = "insert into customers(customer_name, mobile_no, operator) values (%s,%s,%s)"
        data = (name,mb_no,operator)
        cur.execute(query,data)
        db.commit()
        print("Customer Added Successfully.....")
        db.close()

    def view_plans(self):
        plan_id = int(input("Enter Plan Id "))
        operator = input("Enter Operator ")
        cur, db = super().cursors()
        cur.execute("select * from recharge_plans where plan_id = %s and operator = %s",(plan_id,operator))
        res = cur.fetchall()
        for i in res:
            print(f"id: {i[0]} Operator: {i[1]} Plan Name: {i[2]} Amount: {i[3]} Validity: {i[4]}")
        db.close()

    def recharge(self):
        mob_no = input("Enter Mobile Number ")
        plan_id = int(input("Enter Plan Id "))
        date = input("Enter Recharge Date ")
        cur, db = super().cursors()
        cur.execute("select mobile_no from customers where mobile_no = %s",(mob_no,))
        res = cur.fetchone()
        mobile_no = res[0]
        cur.execute("select plan_name,amount from recharge_plans where plan_id = %s",(plan_id,))
        res1 = cur.fetchone()
        plan_name = res1[0]
        tax = 10/100
        amount = res1[1] + tax
        cur.execute("insert into recharge_history(mobile_no, plan_name, amount, recharge_date) values (%s,%s,%s,%s)",(mobile_no,plan_name,amount,date))
        db.commit()
        print(f"Recharge Successfull and your amount is {amount}")
        db.close()



