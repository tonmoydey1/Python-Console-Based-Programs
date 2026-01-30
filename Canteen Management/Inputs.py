from  functionality import *



def inputs_():
    while True:
        print("Welcome To Canteen Managent System...................")
        print("\n1. Add Food Items\n2. View Food Items\n3. Place Order\n4. View Order\n5. Exit")

        ch = input("Enter Choice ")

        if ch == "1":
            f = Foods()
            f.add_food_items()
        elif ch == "2":
            f = Foods()
            f.view_food_items()
        elif ch == "3":
            f = Foods()
            f.order_food()
        elif ch == "4":
            pass
        elif ch == "5":
            print("Thank You For Visit...")
            break