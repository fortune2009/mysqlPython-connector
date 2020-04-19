import mysql.connector
from mysql.connector import Error


def connect_fetch():
    """Function to fetch query from a database table"""

    link = None
    try:
        link = mysql.connector.connect(host="localhost",
                                       database="demo",
                                       user="oscar",
                                       password="password",
                                       auth_plugin="mysql_native_password")

        print("Connecting to database server...")
        if link.is_connected:
            print("Connected to database server...")

            mysql_select_query = "select * from human;"
            cursor = link.cursor()
            cursor.execute(mysql_select_query)
            record = cursor.fetchall()
            print("Total amount of human table rows: ", cursor.rowcount)

            print("\nPrinting records: ")
            for row in record:
                print("humanId: ", row[0])
                print("name: ", row[1])
                print("color: ", row[2])
                print("gender: ", row[3])
                print("genotype: ", row[4], '\n')

    except Error as e:
        print("Connection could not not be established\n\tTry again", e)
    finally:
        if link is not None and link.is_connected():
            link.close()
            print("Database is closing...")


# Invoking the method declared above
connect_fetch()
