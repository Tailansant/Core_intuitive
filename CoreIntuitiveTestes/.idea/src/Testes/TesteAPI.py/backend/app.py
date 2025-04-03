from flask import Flask, jsonify
from operator_service import OperatorService
from csv_loader import CsvLoader

app = Flask(__name__)

csv_loader = CsvLoader('datas/operators.csv')
operator_service = OperatorService(csv_loader)

@app.route('/')
def home():
    return "Welcome to the Flask server! Access specific routes to interact with the API."

@app.route('/search')
def search_operators():

    search_results = operator_service.search_operators('ADRESS')
    return jsonify(search_results)


app.run(debug=True)
