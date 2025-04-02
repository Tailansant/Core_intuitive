from flask import jsonify

class OperatorService:
    def __init__(self, data_loader):
        self.data_loader = data_loader
        self.operators = self.data_loader.load_data()

    def search_operators(self, query):
        if self.operators is None:
            print("Erro: Dados não carregados. Verifique o arquivo CSV.")
            return []

        if 'Razao_Social' not in self.operators.columns:
            print("Coluna 'Razao_Social' não encontrada!")
            return []

        print(f"Buscando por: {query}")
        results = self.operators[self.operators['Razao_Social'].str.contains(query, case=False, na=False)]

        print(f"Resultados encontrados: {len(results)}")

        return results.to_dict(orient='records') 