import random

from db_connection import connect

pnr = random.randint(1,10)
price = 2500
def book_tickets():
    name = input("Enter your name ")
    age = input("Enter your age ")
    train_no = input("Enter Train Number ")
    train_name = input("Enter Train Name ")
    source = input("Enter source ")
    des= input("Enter destination ")

    db = connect()
    cursor = db.cursor()
    query = "insert into details(pnr_no, passenger_name, age, train_no,train_name,source,destination) values(%s,%s,%s,%s,%s,%s,%s)"
    data  = (pnr,name,age,train_no,train_name,source,des)
    cursor.execute(query,data)

    db.commit()
    print(f"paid Rs{price+30+100} and Ticket Booked success")
    db.close()

def booking_details():
    slt_id = int(input("Enter pnr no. to view booking "))
    db = connect()
    cursor = db.cursor()

    cursor.execute("select * from details where pnr_no = %s",(slt_id,))
    result = cursor.fetchall()
    for i in result:
        print(i)


    db.close()

def cancel_ticket():
    slt_id = int(input("Enter pnr no. to cancel booking "))
    db = connect()
    cursor = db.cursor()

    cursor.execute("delete from details where pnr_no = %s",(slt_id,))
    print("ticket cancelled successfully")


def trains():
    db = connect()
    cursor = db.cursor()

    cursor.execute("select train_name from details")
    result = cursor.fetchall()
    for i in result:
        print(i)
    db.close()

