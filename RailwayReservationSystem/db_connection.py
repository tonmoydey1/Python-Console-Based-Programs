import  mysql.connector as conn

def connect():
    return conn.connect(host="localhost",user="root",password="12345",database="railwayreservation")
