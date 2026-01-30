from handleOperation import *

def handle_input():
    while True:
        print("1: View Products")
        print("2: Add Product")
        print("3: View Cart")
        print("4: Exit")
        ch = input("Enter Choice ")

        if ch == "1":
            show_products()
        elif ch == "2":
            add_to_cart()
        elif ch == "3":
            view_cart()
        elif ch == "4":
            print("Thanks for visiting")
            break

