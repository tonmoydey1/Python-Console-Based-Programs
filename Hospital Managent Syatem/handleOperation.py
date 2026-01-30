import random
from  Db import connect


hos_id = random.randint(100000, 300000)
def add_patient():
    name = input("Enter Patient name ")
    age = int(input("Enter Patient age "))
    ph = input("Enter Patient Ph No. ")
    gender = input("Enter Patient Gender ")
    disease = input("Enter Disease ")
    doc_name = input("Enter Doctor Name ")
    department = input("""Enter Doctors' Department""")
    admitted = input("Is Admitted ? ")

    db = connect()
    cursor = db.cursor()
    query = "insert into patient(hos_id,name,age,ph,gender,disease,doc_name,department,admitted) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (hos_id,name,age,ph,gender,disease,doc_name,department,admitted)
    cursor.execute(query,data)
    db.commit()
    print("Data Inserted Successfully........")

