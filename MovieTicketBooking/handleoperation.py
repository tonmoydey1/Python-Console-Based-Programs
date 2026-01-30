import mysql.connector as conn

class DBConnection:
    def connect(self):
        return conn.connect(host = "localhost", user = "root", password = "12345", database = "movie_db")
    def cur_connection(self):
        db = self.connect()
        cur = db.cursor()
        return db,cur


class Operations(DBConnection):

    def register(self):
        username = input("Enter Username ")
        password = input("Enter password ")
        db, cur = super().cur_connection()
        cur.execute("select username from user where username = %s",(username,))
        res = cur.fetchone()
        if res is not None:
            for i in res:
                print(f"{res[0]} already exists")
        else:
            query = "insert into user(username,password) values (%s,%s)"
            data  = (username,password)
            cur.execute(query,data)
            db.commit()
            print("Registered Successfully....")
        db.close()

    def login(self):
        username = input("Enter Username ")
        password = input("Enter password ")
        db, cur = super().cur_connection()
        cur.execute("select username from user where username=%s and password=%s",(username,password))
        res = cur.fetchall()
        if res is not None:
            for i in res:
                print(f"Welcome {i[0]} !")
                return res[0]
        else:
            print("Invalid Username And Password")
            return None
        db.close()


    def add_movies(self):
        movie_name = input("Enter Movie Name ")
        show_time = input("Enter Show Time ")
        ticket = int(input("Enter Ticket Price "))
        seat = int(input("Enter Available Seat "))

        db,cur = super().cur_connection()

        query = "insert into movies(movie_name,show_time,ticket_price,avilable_seats) values (%s,%s,%s,%s)"
        data = (movie_name,show_time,ticket,seat)
        cur.execute(query,data)
        db.commit()
        print("Data Inserted Successfully")
        db.close()

    def view_movies(self):
        movie_id = int(input("Enter Movie Id "))
        db, cur = super().cur_connection()
        cur.execute("select * from movies where movie_id = %s",(movie_id,))
        res = cur.fetchall()
        if res is not None:
            for i in res:
                print(f"Available Movies: {i[0],i[1],i[2],i[3],i[4]}")
        else:
            print("Enter Valid Id.....")
        db.close()
    def book_ticket(self):
        movie_id = int(input("Enter Movie Id "))
        seats_booked = int(input("Enter Seats Booked "))
        booking_date = input("Enter Booking Date ")
        db, cur = super().cur_connection()
        cur.execute("select movie_name, ticket_price,available_seats from movies where movie_id = %s",(movie_id,))
        res = cur.fetchone()
        movie_name = res[0]
        ticket_price = res[1]
        tax = round(10/100,0)
        tot_price = ticket_price + tax
        cur.execute("insert into bookings(movie_name,seats_booked,total_amount,booking_date) values (%s,%s,%s,%s)",(movie_name,seats_booked,tot_price,booking_date))
        print(f"Your Bill Is Rs.{tot_price}")
        cur.execute("update movies set available_seats = available_seats - %s", (seats_booked,))
        db.commit()

        db.close()

