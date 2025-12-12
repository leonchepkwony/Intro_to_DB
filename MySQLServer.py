import mysql.connector 
from mysql.connector import Error
try:
    db = mysql.connector.connect(
        host = 'localhost',
        user ='root',
        password = 'Leon2!@#' 
    )

    if db.is_connected():
        mycursor = db.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

        mycursor.execute("SHOW DATABASES")

        mycursor.close()
        db.close()

except Error as e:
    print("Error while creating Database: ", e)

