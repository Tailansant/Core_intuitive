from entities.downloader import Downloader
from entities.database_connector import DatabaseConnector
from entities.table_creator import TableCreator
from entities.csv_importer import CsvImporter
from entities.query_executor import QueryExecutor

def main():
    downloader = Downloader()
    db_connector = DatabaseConnector(host="localhost", user="root", password="Ocaosperfeito1#", database="database_teste")
    table_creator = TableCreator(db_connector)
    csv_importer = CsvImporter(db_connector)
    query_executor = QueryExecutor(db_connector)

    operators_url = 'https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv'
    financial_data_urls = [
        'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/',
        'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/'
    ]

    downloader.download_file(operators_url, 'operators.csv')
    for url in financial_data_urls:
        year = url.split('/')[-2]
        downloader.download_file(url, f'financial_data_{year}.csv')

    table_creator.create_tables()

    csv_importer.import_csv('datas/operators.csv', 'health_plan_operators')
    for url in financial_data_urls:
        year = url.split('/')[-2]
        csv_importer.import_csv(f'datas/financial_data_{year}.csv', 'health_expenses')

    last_quarter_query = """
    SELECT 
        o.operator_name,
        SUM(e.expense_value) AS total_expense
    FROM 
        health_expenses e
    JOIN 
        health_plan_operators o ON e.operator_cnpj = o.cnpj
    WHERE 
        e.expense_category = 'EVENTS/CLAIMS KNOWN OR REPORTED FOR MEDICAL HOSPITAL ASSISTANCE'
        AND e.quarter BETWEEN '2024-10-01' AND '2024-12-31'
    GROUP BY 
        o.operator_name
    ORDER BY 
        total_expense DESC
    LIMIT 10;
    """
    query_executor.execute_query(last_quarter_query)

if __name__ == "__main__":
    main()