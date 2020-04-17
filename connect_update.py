import mysql.connector as myquery
from mysql.connector import Error


def connect_update():
    """Here we create a connection and update a table"""

    connect_data = None
    try:
        connect_data = myquery.connect(host="localhost",
                                       database="demo",
                                       user="oscar",
                                       password="password",
                                       auth_plugin="mysql_native_password")

        print("Connecting at the Moment")

        if connect_data.is_connected:
            print("Connection established")
            db_cursor = connect_data.cursor()

            # Now lets query to database for data-set validation
            data_query = "select * from human where HumanId=1002;"

            # Use the sql function cursor to link and validate query
            db_cursor.execute(data_query)

            # Lets fetch a tuple with a variable from the db_cursor
            tupler = db_cursor.fetchone()
            print(tupler)

            # Updating the row and creating a query
            sql_query_update = "update human set Sex = 'Female' where HumanId = 1002"

            db_cursor.execute(sql_query_update)

            connect_data.commit()
            print("record Updated Successfully")

    except Error as e:
        print("Connection failed due to the following: ", e)
    finally:
        if connect_data is not None and connect_data.is_connected:
            connect_data.close
            print("Disconnected from database")


# function caller is below
connect_update()
