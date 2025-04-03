class CsvImporter:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def import_csv(self, filepath, table_name):
        """Importa dados CSV para o banco de dados"""
        try:
            query = f"""
            LOAD DATA LOCAL INFILE '{filepath}'
            INTO TABLE {table_name}
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 LINES;
            """
            connection = self.db_connector.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                print(f"Data from {filepath} imported into {table_name} successfully!")
                self.db_connector.close(connection)
        except Exception as e:
            print(f"Error importing CSV {filepath}: {e}")