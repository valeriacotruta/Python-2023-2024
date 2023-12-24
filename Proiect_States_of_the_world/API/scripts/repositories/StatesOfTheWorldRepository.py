from API.scripts.models import DatabaseConnection as Db
from mysql.connector import Error


class StatesOfTheWorldRepository:
    def __init__(self):
        self.database = Db.DatabaseConnection()
        self.database_connection = self.database.get_database_connection()

    def insert_new_state(self, state):
        try:
            connection_cursor = self.database_connection.cursor()
            query = "INSERT INTO states (name, capital_name, population, density, surface, political_regime)VALUES(%s, %s, %s, %s, %s, %s)"
            values = (
                state.name, state.capital_name, state.population, state.density, state.surface, state.political_regime)
            connection_cursor.execute(query, values)
            self.database_connection.commit()
            print(connection_cursor.rowcount, "record inserted into states table.")
        except Error as exception:
            print("The insertion into states table failed!", exception)

    def insert_state_neighbours(self, state):
        try:
            connection_cursor = self.database_connection.cursor()
            for neighbour in state.neighbours:
                query = "INSERT INTO neighbours (neighbour, state_id)VALUES(%s, %s)"
                values = (neighbour, state.id)
                connection_cursor.execute(query, values)
                self.database_connection.commit()
                print(connection_cursor.rowcount, "record inserted into neighbours table.")
        except Error as exception:
            print("The insertion into neighbours table failed!", exception)

    def insert_state_official_languages(self, state):
        try:
            connection_cursor = self.database_connection.cursor()
            for language in state.spoken_languages:
                query = "INSERT INTO official_languages (spoken_language, state_id)VALUES(%s, %s)"
                values = (language, state.id)
                connection_cursor.execute(query, values)
                self.database_connection.commit()
                print(connection_cursor.rowcount, "record inserted into official_languages table.")
        except Error as exception:
            print("The insertion into official_languages table failed!", exception)

    def insert_state_time_zones(self, state):
        try:
            connection_cursor = self.database_connection.cursor()
            for time_zone in state.time_zones:
                query = "INSERT INTO time_zones (time_zone, state_id)VALUES(%s, %s)"
                values = (time_zone, state.id)
                connection_cursor.execute(query, values)
                self.database_connection.commit()
                print(connection_cursor.rowcount, "record inserted into time_zones table.")
        except Error as exception:
            print("The insertion into time_zones table failed!", exception)

    def get_state_id(self, state_name):
        try:
            connection_cursor = self.database_connection.cursor()
            query = "SELECT id FROM states WHERE name = %s"
            values = (state_name,)
            connection_cursor.execute(query, values)
            state_id = connection_cursor.fetchall()
            return state_id[0][0]
        except Error as exception:
            print("SELECT id FROM states WHERE name = %s failed!", exception)
