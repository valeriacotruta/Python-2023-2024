# from ..models import DatabaseConnection as Db
# from mysql.connector import Error
#
#
# class StatesOfTheWorldRepository:
#     def __init__(self):
#         self.database = Db.DatabaseConnection()
#         self.database_connection = self.database.get_database_connection()
#
#     def insert_new_state(self, state):
#         try:
#             connection_cursor = self.database_connection.cursor()
#             query = "INSERT INTO states (name,capital_name, population,density , surface ,neighbours,spoken_language,time_zone, political_regime)VALUES( ?,?,?,?,?,?,?,?)"
#             values = (state.name, state.capital_name, state.population, state.density, state.surface, state.neighbours,
#                       state.spoken_language, state.time_zone, state.political_regime)
#             connection_cursor.execute(query, values)
#             self.database_connection.commit()
#             print(connection_cursor.rowcount, "record inserted.")
#         except Error as exception:
#             print("The insertion failed!", exception)
