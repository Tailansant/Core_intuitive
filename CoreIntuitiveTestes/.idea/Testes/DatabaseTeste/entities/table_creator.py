class TableCreator:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def create_tables(self):
        """Criação de tabelas no banco de dados"""
        create_operators_table_query = """
        CREATE TABLE IF NOT EXISTS health_plan_operators (
            id INT AUTO_INCREMENT PRIMARY KEY,
            operator_name VARCHAR(255),
            cnpj VARCHAR(20) UNIQUE
        );
        """
        create_expenses_table_query = """
        CREATE TABLE IF NOT EXISTS health_expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            operator_cnpj VARCHAR(20),
            expense_value DECIMAL(15, 2),
            expense_category VARCHAR(255),
            quarter DATE
        );
        """

        connection = self.db_connector.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(create_operators_table_query)
            cursor.execute(create_expenses_table_query)
            connection.commit()
            self.db_connector.close(connection)
            print("Tables created successfully!")