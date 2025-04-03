import pandas as pd

class CsvLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            df = pd.read_csv('datas/operators.csv', delimiter=';')
            print(f"Dados carregados com sucesso! Colunas: {df.columns}")
            return df
        except Exception as e:
            print(f"Erro ao carregar o CSV: {e}")
            return None
