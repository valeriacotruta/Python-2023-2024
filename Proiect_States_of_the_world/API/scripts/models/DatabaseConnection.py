import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self):
        try:
            self.mysql_database_connection = mysql.connector.connect(host='localhost',
                                                                     database='states_of_the_world',
                                                                     user='root',
                                                                     password='valeriacotruta')
            if self.mysql_database_connection.is_connected():
                database_response = self.mysql_database_connection.get_server_info()
                print("Your connection to the database succeed!")
        except Error as exception:
            print("Your connection to the database failed!", exception)

    def close_connection(self):
        if self.mysql_database_connection.is_connected():
            self.mysql_database_connection.close()
            print("The connection is closed.")

    def get_database_connection(self):
        return self.mysql_database_connection