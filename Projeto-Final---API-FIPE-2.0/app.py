from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)

CORS(app)

API = "https://parallelum.com.br/fipe/api/v1"



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/marcas/<tipo_veiculo>", methods=["GET"])
def get_marcas(tipo_veiculo):
    response = requests.get(f"{API}/{tipo_veiculo}/marcas")
    return jsonify(response.json())

@app.route("/modelos/<tipo_veiculo>/<id_marca>", methods=["GET"])
def get_modelos(tipo_veiculo, id_marca):
    response = requests.get(f"{API}/{tipo_veiculo}/marcas/{id_marca}/modelos")
    return jsonify(response.json())

@app.route("/anos/<tipo_veiculo>/<id_marca>/<id_modelo>", methods=["GET"])
def get_anos(tipo_veiculo, id_marca, id_modelo):
    response = requests.get(f"{API}/{tipo_veiculo}/marcas/{id_marca}/modelos/{id_modelo}/anos")
    return jsonify(response.json())

@app.route("/preco/<tipo_veiculo>/<id_marca>/<id_modelo>/<ano>", methods=["GET"])
def get_preco(tipo_veiculo, id_marca, id_modelo, ano):
    response = requests.get(f"{API}/{tipo_veiculo}/marcas/{id_marca}/modelos/{id_modelo}/anos/{ano}")
    print(response.json())  # Tive um bug nesse final da API , então o print é para retornar o que estava aparecendo e quais parametros deveria alterar no front END - 18/11/2024
    return jsonify(response.json()) 


if __name__ == "__main__":
    app.run(debug=True)
