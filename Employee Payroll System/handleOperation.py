from conn import connect as conn

def add_employee():
    emp_id = int(input("Enter employee id "))
    name = input("Enter employee name ")
    age = int(input("Enter Age "))
    department = input("Enter employee department ")
    salary = int(input("Enter employee salary "))

    db = conn()
    cursor = db.cursor()

    query = "insert into emp(emp_id,name,age,department,salary) values(%s,%s,%s,%s,%s)"
    data = (emp_id,name,age,department,salary)

    cursor.execute(query,data)
    db.commit()
    print("Data Inserted Successfully")
    db.close()
def view_employee():
    view_id = int(input("Enter Employee Id "))

    db = conn()
    cursor = db.cursor()
    cursor.execute("select * from emp where emp_id = %s",(view_id,))

    res = cursor.fetchall()

    for i in res:
        print(i[0],i[1],i[2],i[3],i[4])
    db.close()

def srch_employee():
    view_id = int(input("Enter Employee Id "))

    db = conn()
    cursor = db.cursor()
    cursor.execute("select * from emp where emp_id = %s", (view_id,))

    emp_res = cursor.fetchall()
    db.close()

    if emp_res:
        print(f"Employee Found {emp_res}")
    else:
        print("Not Found")

def upd_employee():
    emp_id = int(input("Enter employee id "))
    name = input("Enter employee name ")
    age = int(input("Enter Age "))
    department = input("Enter employee department ")
    salary = int(input("Enter employee salary "))

    db = conn()
    cursor = db.cursor()
    cursor.execute("Update emp set name = %s, age = %s, department = %s, salary = %s where emp_id = %s",(emp_id,name,age,department,salary))
    res  = cursor.fetchall()
    if res:
        print()
    db.commit()
    print("Data Updated Successfully")
    db.close()

def delete_employee():
    emp_id = int(input("Enter employee id "))
    db = conn()
    cursor = db.cursor()
    cursor.execute("Delete from emp where emp_id=%s",(emp_id,))
    db.commit()
    print("Data Deleted Successfully")
    db.close()





