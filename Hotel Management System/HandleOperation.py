import random


import mysql.connector as conn

class DatabaseConn:
    def connect(self):
        return conn.connect(host="localhost",user="root",password="12345",database="hotelmanagementsystem")
class RoomManagement(DatabaseConn):
    def add_room(self):
        room_type = input("Enter Room Type ")
        room_price = int(input("Enter Room Price "))
        room_status = input("Enter Room Status (Vacant/Full) ")

        db = self.connect()
        cursor = db.cursor()
        query = "insert into rooms(room_type,price,status) values (%s,%s,%s)"
        data = (room_type,room_price,room_status)
        cursor.execute(query,data)
        db.commit()
        print("Room Added Successfully......")
        db.close()

    def view_room(self):
        room_id = int(input("Enter Room Id "))

        db = self.connect()
        cursor = db.cursor()
        query = "select * from rooms where room_id = %s"
        data = (room_id,)
        cursor.execute(query,data)
        res = cursor.fetchall()
        if res:
            for i in res:
                print(i[0], i[1], i[2], i[3])
        else:
            print()
        db.close()

    def update_room(self):
        room_id = int(input("Enter Room Id "))
        room_type = input("Enter Room Type ")
        room_price = int(input("Enter Room Price "))
        room_status = input("Enter Room Status (Vacant/Full) ")

        db = self.connect()
        cursor = db.cursor()

        cursor.execute("SELECT room_id FROM rooms WHERE room_id = %s", (room_id,))
        res = cursor.fetchone()

        if res is None:
            print("Room not available")
        else:

            query = "update rooms set room_type = %s, price = %s, status = %s where room_id = %s"
            data = (room_type,room_price,room_status,room_id)
            cursor.execute(query,data)
            db.commit()
            print("Room Updated Successfully")
            db.close()

    def delete_room(self):
        room_id = int(input("Enter Room Id "))

        db = self.connect()
        cursor = db.cursor()
        query = "delete from rooms where room_id = %s"
        data = (room_id,)
        cursor.execute(query, data)
        db.commit()
        print("Room Deleted Successfully")
        db.close()

    def room_avilability(self):
        room_id = int(input("Enter Room Id "))

        db = self.connect()
        cursor = db.cursor()
        query = "select status from rooms where room_id = %s"
        data = (room_id,)
        cursor.execute(query,data)
        res = cursor.fetchall()
        for i in res:
            print(f"Room Avilability: {i[0]}")
        db.close()

class CustomerManagement(DatabaseConn):
    def add_customer(self):
        cust_id = random.randint(10000,50000)
        name = input("Enter Customer Name ")
        phone = input("Enter Customer Ph. number ")
        id_proof = input("Enter Id Type ")

        db = self.connect()
        cursor = db.cursor()
        query = "insert into customers(customer_id,name,phone,id_proof) values (%s,%s,%s,%s)"
        data = (cust_id, name, phone, id_proof)
        cursor.execute(query,data)
        db.commit()

        print("Customer details added successfully.......")
        db.close()
    def view_customer(self):
        pass

class BookingManagement(DatabaseConn):
    def book_room(self):
        global total
        booking_id = random.randint(5000,6000)
        room_id = int(input("Enter Room Id "))
        check_in_date = input("Enter Checkin Date")
        check_out_date = input("Enter Checkout Date")



        db = self.connect()
        cursor = db.cursor()

        cursor.execute("select room_type from rooms ")
        res = cursor.fetchall()
        total = 0
        if res:

            total = 4000
        elif res:

            total = 5000
        elif res:

            total = 7000
        elif res:

            total = 9000

        cust_id = cursor.lastrowid

        query = "insert into bookings(booking_id,customer_id,room_id,check_in,check_out,total_amount) values(%s,%s,%s,%s,%s,%s)"
        data = (booking_id,cust_id,room_id,check_in_date,check_out_date,total)
        cursor.execute(query,data)

        db.commit()
        print(("Room Booked Successfully"))
        db.close()






