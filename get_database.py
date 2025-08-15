import mysql.connector

def get_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='users'
    )