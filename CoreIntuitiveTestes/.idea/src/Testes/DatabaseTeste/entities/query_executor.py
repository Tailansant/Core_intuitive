class QueryExecutor:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def execute_query(self, query):
        """Executa uma consulta SQL no banco de dados"""
        try:
            connection = self.db_connector.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
                self.db_connector.close(connection)
        except Exception as e:
            print(f"Error executing query: {e}")