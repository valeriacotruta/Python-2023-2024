import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    """
    A class to represent the connection to the database.

    Attributes
    ----------
    mysql_database_connection : MySQLConnection
       creates an instance of MySQLConnection using mysql.connector.connect(*args: Any, **kwargs: Any
        ) -> Union[PooledMySQLConnection, MySQLConnection, CMySQLConnection]:

    Methods
    -------
    get_database_connection(self):
        Returns the connection to the database.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the DatabaseConnection object.
        Tries to create a connection to the database. If it fails, an error is raised.
        """
        try:
            self.mysql_database_connection = mysql.connector.connect(host='localhost',
                                                                     database='states_of_the_world',
                                                                     user='root',
                                                                     password='valeriacotruta')
            if self.mysql_database_connection.is_connected():
                pass
                # print("Your connection to the database succeed!")
        except Error as exception:
            print("Your connection to the database failed!", exception)

    def get_database_connection(self):
        """
        Returns the connection to the database.

        :return: MySQLConnection
        """
        return self.mysql_database_connection
