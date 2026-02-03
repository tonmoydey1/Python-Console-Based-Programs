import mysql.connector as conn

class DBConnection:
    def connect(self):
        return conn.connect(host="localhost",user = "root", password = "12345", database = "waterbill_db")
    def cursors(self):
        db = self.connect()
        cur = db.cursor()
        return db,cur

class Operations(DBConnection):
    def add_consumer(self):
         consumer_name = input("Enter Consumer Name ")
         house_no = int(input("Enter House Number "))
         mobile_no = input("Enter Mobile Number ")
         db,cur = super().cursors()
         query = "insert into consumers(consumer_name, house_no, mobile_no) values(%s,%s,%s)"
         data = (consumer_name,house_no,mobile_no)
         cur.execute(query,data)
         db.commit()
         print("Customer inserted successfully")
         db.close()
    def add_usage(self):
        consumer_id = int(input("Enter consumer "))
        units_used = int(input("Enter units used "))
        month = input("Enter usage month ")
        db, cur = super().cursors()
        cur.execute("select consumer_id from consumers where consumer_id = %s",(consumer_id,))
        res = cur.fetchone()

        if res is None:
            print("Consumer id not available........")
        else:
            consume_id = res[0]
            cur.execute("insert into water_usage(consumer_id, units_used, usage_month) values(%s,%s,%s)",(consume_id,units_used,month))
            db.commit()
            print("Water usage entered successfully")
            db.close()
    def generate_bill(self):
        consumer_id = int(input("Enter consumer id "))
        amount = int(input("Enter amount "))
        bill_status = input("Enter bill status ")
        bill_date = input("Enter bill date ")
        db, cur = super().cursors()
        cur.execute("select units_used from water_usage where consumer_id = %s",(consumer_id,))
        res = cur.fetchone()
        unit_used = res[0]
        tot_amount = unit_used * amount
        cur.execute("insert into bills(consumer_id, units_used, amount, bill_status, bill_date) values(%s,%s,%s,%s,%s)",
                    (consumer_id,unit_used,tot_amount,bill_status,bill_date))
        db.commit()
        print(f"Bill generated successfully and the amount is {tot_amount}")
        db.close()

    def pay_bill(self):
        consumer_id = int(input("Enter consumer id "))
        date = input("Enter payment date ")
        payment_mode = input("Enter payment mode ")
        db, cur = super().cursors()
        cur.execute("select amount from bills where consumer_id = %s and bill_status = 'unpaid'",(consumer_id,))
        res = cur.fetchone()
        for i in res:
            print(f" Your bill is Rs.{i}")
        amount = res[0]
        cur.execute("insert into payments(consumer_id, amount, payment_date, payment_mode) values (%s,%s,%s,%s)",(consumer_id,amount,date,payment_mode))
        cur.execute("update bills set bill_status = 'paid' where consumer_id = %s",(consumer_id,))
        db.commit()
        print(f"Bill of Rs.{amount} is paid successfully")
        db.close()
    def view_payments(self):
        consumer_id = int(input("Enter consumer id "))
        db, cur = super().cursors()
        cur.execute("select * from payments where consumer_id = %s",(consumer_id,))
        res = cur.fetchall()
        if res:
            for i in res:
                print(i[0],i[1],i[2],i[3],i[4])
        else:
            print("consumer_id not found ")
        db.close()







