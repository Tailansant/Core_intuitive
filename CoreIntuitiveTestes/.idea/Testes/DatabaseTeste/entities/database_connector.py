import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """Estabelece a conexão com o banco de dados MySQL e garante que LOCAL está habilitado."""
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                allow_local_infile=True  
            )

            cursor = connection.cursor()
            cursor.execute("SET GLOBAL local_infile = 1;")

            if connection.is_connected():
                print("Connection to the database successful!")
                return connection

        except Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    def close(self, connection):
        """Fecha a conexão com o banco de dados."""
        if connection and connection.is_connected():
            connection.close()
            print("Database connection closed.")