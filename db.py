import mysql.connector

def get_connection():
    return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='PROGRA_2-2P',
            ssl_disabled=True
        )