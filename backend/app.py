from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def calcular_cashback(valor_compra, percentual_desconto, tipo_cliente):
    valor_final = valor_compra * (1 - percentual_desconto / 100)

    cashback_base = valor_final * 0.05
    cashback_total = cashback_base

    if tipo_cliente.lower() == "vip":
        bonus_vip = cashback_base * 0.10
        cashback_total += bonus_vip

    if valor_final > 500:
        cashback_total *= 2

    return round(cashback_total, 2)

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            tipo_cliente TEXT,
            valor REAL,
            cashback REAL
        )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return"API de Cashback funcionando"

@app.route("/cashback", methods=["POST"])
def cashback():
    data = request.json

    if not data:
        return jsonify({"erro": "JSON inválido ou ausente"}), 400

    valor = data.get("valor")
    desconto = data.get("desconto")
    tipo = data.get("tipo_cliente")

    if valor is None or desconto is None or tipo is None:
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    ip = request.remote_addr

    cashback = calcular_cashback(valor, desconto, tipo)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO consultas (ip, tipo_cliente, valor, cashback) VALUES (?, ?, ?, ?)", 
        (ip, tipo, valor,cashback)                                       
    )

    conn.commit()
    conn.close()

    return jsonify({"cashback": cashback})

@app.route("/historico", methods=["GET"])
def historico():
    ip = request.remote_addr

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT tipo_cliente, valor, cashback FROM consultas WHERE ip = ?",
        (ip,)
    )

    dados = cursor.fetchall()
    conn.close()

    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)