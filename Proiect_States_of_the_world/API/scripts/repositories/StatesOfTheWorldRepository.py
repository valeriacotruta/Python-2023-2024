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
            print("SELECT id FROM states WHERE name ____ failed!", exception)

    def get_top_10_states_by(self, argument):
        try:
            connection_cursor = self.database_connection.cursor()
            query = f"SELECT * FROM states ORDER BY {argument} DESC LIMIT 10"
            connection_cursor.execute(query)
            rows = connection_cursor.fetchall()
            return rows
        except Error as exception:
            print("SELECT * FROM states ORDER BY ____ failed!", exception)

    def get_state_by_id(self, state_id):
        try:
            connection_cursor = self.database_connection.cursor()
            query = "SELECT * FROM states WHERE id = %s"
            values = (state_id,)
            connection_cursor.execute(query, values)
            state = connection_cursor.fetchone()
            return state
        except Error as exception:
            print("SELECT * FROM states WHERE id ____ failed!", exception)

    def get_states_by_language(self, language):
        try:
            connection_cursor = self.database_connection.cursor()
            query = "SELECT state_id FROM official_languages WHERE spoken_language LIKE %s"
            values = (("%" + language + "%"),)
            connection_cursor.execute(query, values)
            rows = connection_cursor.fetchall()
            return [state_id[0] for state_id in rows]
        except Error as exception:
            print("SELECT state_id FROM official_languages WHERE spoken_language LIKE ____ failed!", exception)

    def get_states_by_time_zone(self, time_zone):
        try:
            connection_cursor = self.database_connection.cursor()
            query = "SELECT state_id FROM time_zones WHERE time_zone LIKE %s"
            values = (("%" + time_zone + "%"),)
            connection_cursor.execute(query, values)
            rows = connection_cursor.fetchall()
            return [state_id[0] for state_id in rows]
        except Error as exception:
            print("SELECT state_id FROM time_zones WHERE time_zone LIKE ____ failed!", exception)

    def get_states_by_neighbour(self, neighbour):
        try:
            connection_cursor = self.database_connection.cursor()
            query = "SELECT state_id FROM neighbours WHERE neighbour LIKE %s"
            values = (("%" + neighbour + "%"),)
            connection_cursor.execute(query, values)
            rows = connection_cursor.fetchall()
            return [state_id[0] for state_id in rows]
        except Error as exception:
            print("SELECT state_id FROM neighbours WHERE neighbour LIKE ____ failed!", exception)

    def get_states_by_political_regime(self, political_regime):
        try:
            connection_cursor = self.database_connection.cursor()
            query = "SELECT id, name FROM states WHERE political_regime LIKE %s"
            values = (("%" + political_regime + "%"),)
            connection_cursor.execute(query, values)
            rows = connection_cursor.fetchall()
            return rows
        except Error as exception:
            print("SELECT name FROM states WHERE political_regime LIKE ____ failed!", exception)
