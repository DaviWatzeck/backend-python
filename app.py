from flask import Flask, jsonify
from flask_cors import CORS
import RPG  # Importe o RPG.py como um módulo

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    start_game()
    return


@app.route('/start', methods=['POST'])
def start_game():
    # Simula pegar o nome do jogador vindo do frontend

    RPG.gameplay()  # Executa a aventura

    return jsonify({"mensagem": "A aventura começou!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
