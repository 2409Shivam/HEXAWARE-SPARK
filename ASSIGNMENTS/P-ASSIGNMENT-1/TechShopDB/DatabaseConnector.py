import mysql.connector

class DatabaseConnector:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def open_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Connected to the database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query, values=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
            print("Query executed successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
