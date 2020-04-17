import mysql.connector as insql
from mysql.connector import Error

def connect_insert():
    ''' this function connect and insert a row in a database'''

    conn= None

    try:
        conn = insql.connect(host="localhost",
                             database="demo",
                             user="oscar",
                             password="ochiabuto2009",
                             auth_plugin="mysql_native_password")
        
        print("Connecting in progress")

        if conn.is_connected:
            print("Connection established with DB")
            db_cursor = conn.cursor()

            #create a variable for targeted sql
            sql = "INSERT INTO Human (HumanId, Name, Color, Sex, Bloodgrup) VALUES (%s, %s, %s, %s, %s)"

            #create a list of values assigned to a variable

            insert_values = [
                              ('1005', 'Grace Harmond', 'Green', 'Female', 'B-'),
                              ('1006', 'Burn Lukwan', 'Ivory', 'Male', 'AB'),
                              ('1007', 'Heshaw Hecman', 'Gold', 'Female', 'O-'),
                              ('1008', 'Jon Bellon', 'Yellow', 'Male', 'A+'),
                              ('1009', 'Kendjo Wimpsey', 'Orange', 'Female', '0+')
                            ]

            #Now a function executeMany function will be used to process these value
            db_cursor.executemany(sql, insert_values)

            #Lets commit to the DB for recent changes
            conn.commit()

            #Print success -m
            print(db_cursor.rowcount, "rows was inserted")

            #close cursor for GC to do its Job
            db_cursor.close

    except Error as warning:
        print("connection failed due to this -> ", warning)
    finally:
        if conn is not None and conn.is_connected:
            conn.close
            print("Disconnected from DB")


#call the insert function
connect_insert()
