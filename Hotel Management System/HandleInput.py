from HandleOperation import *

def handle_inp():
    while True:
        print(".........Welcome To Hotel Management System........")
        print("\n1. Add Room\n2. View Rooms\n3. Update Rooms\n4. Delete Rooms\n5. Room Avilability\n6. Add Customers\n7. Bookings")

        ch = input("Enter Your Choice ")

        if ch == "1":
            rm = RoomManagement()
            rm.add_room()
        elif ch == "2":
            rm = RoomManagement()
            rm.view_room()
        elif ch == "3":
            rm = RoomManagement()
            rm.update_room()
        elif ch == "4":
            rm = RoomManagement()
            rm.delete_room()
        elif ch == "5":
            rm = RoomManagement()
            rm.room_avilability()
        elif ch == "6":
            cm = CustomerManagement()
            cm.add_customer()
        elif ch == "7":
            cm = BookingManagement()
            cm.book_room()