import random

from db import connect

db = connect()
cursor = db.cursor()

def show_products():
    cursor.execute("select * from products")
    product = cursor.fetchall()
    print("\nAvilable Product")
    print("-" * 30)
    for p in product:
        print(f"{p[0]} {p[1]} {p[2]}")
def add_to_cart():
    pid = int(input("Enter product id"))
    qty = int(input("Enter quantity"))

    cursor.execute("insert into cart(product_id,quantity) values(%s,%s)",(pid,qty))
    db.commit()
    print("Product Added To Cart")
def view_cart():
    query = ("""select products.name,products.price,cart.quantity from cart
             join products on cart.id = products.id""")

    cursor.execute(query)
    items = cursor.fetchall()

    if not items:
        print("\nCart is empty")
        return

    total = 0
    print("\nYour Cart")
    print("-----------------------------------------------------------")

    for item in items:
        name,price,qty = item
        cost = price * qty
        total += cost
        print(f"{name} Qty: {qty} ${price}")

        print(f"Total Bill {total}")


