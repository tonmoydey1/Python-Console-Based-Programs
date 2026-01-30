import mysql.connector as conn

def connect():
    return conn.connect(host="localhost",username = "root", password = "12345", database = "hospitalmanagementsystem")