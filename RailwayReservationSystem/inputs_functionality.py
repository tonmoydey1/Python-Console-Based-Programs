from bookingOperations import *

def operations():
    while True:
        print("1. Book tickets")
        print("2. Cancel tickets")
        print("3. Check booking status")
        print("4. View available trains")

        ch = input("Enter Choice ")
        if ch == "1":
            book_tickets()
        elif ch == "2":
            cancel_ticket()
        elif ch == "3":
            booking_details()
        elif ch == "4":
            trains()
        else:
            print("Wrong Choice !!!! Please try again")