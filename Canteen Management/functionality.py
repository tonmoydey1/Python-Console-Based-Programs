import mysql.connector as conn

class DatabaseConn:
    def connect(self):
        return conn.connect(host="localhost",user="root",password="12345",database="canteen_management_db")


class Foods(DatabaseConn):
    def add_food_items(self):
        name = input("Enter Food Name ")
        price = int(input("Enter Price "))

        db = self.connect()
        cursor = db.cursor()
        query = "insert into food(food_name,price) values (%s,%s)"
        data = (name,price)
        cursor.execute(query,data)
        db.commit()
        print("Food Inserted Successfully......")

    def view_food_items(self):
        food_id = input("Enter Food Id ")
        db = self.connect()
        cursor = db.cursor()
        query = "select * from food where food_id = %s"
        data = (food_id,)
        cursor.execute(query,data)
        res = cursor.fetchall()
        if res:
            for i  in res:
                print(f"Id: {i[0]} Name: {i[1]} Price Rs.{i[2]}")
        db.close()

    def order_food(self):
        food_id = input("Enter Food Id ")
        qty = int(input("Enter Quantity "))
        db = self.connect()
        cursor = db.cursor()

        cursor.execute("select food_name, price from food where food_id = %s",(food_id,))
        res = cursor.fetchone()

        if res:
            name = res[0]
            price = res[1]
            total = price * qty

            query = "insert into orders(food_name,quantity,total_price) values (%s,%s,%s)"
            data = (name, qty, total)

            cursor.execute(query,data)
            db.commit()
            print("Order Booked and Your Total Bill is: ",total)
            db.close()




