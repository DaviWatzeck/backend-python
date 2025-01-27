from flask import Flask, jsonify, request
from flask_cors import CORS
import RPG  # Importe o RPG.py como um módulo

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({"mensagem": "Backend para RPG funcionando!"})


@app.route('/start', methods=['POST'])
def start_game():
    # Simula pegar o nome do jogador vindo do frontend
    data = request.json
    player_name = data.get('player_name', 'Jogador Desconhecido')

    # Usa a função do RPG.py
    RPG.player_name = player_name
    RPG.gameplay()  # Executa a aventura

    return jsonify({"mensagem": f"A aventura começou para {player_name}!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
