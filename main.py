from flask import Flask, make_response, jsonify, request
from bd import tarefas

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # Para manter a ordem das chaves no JSON

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return make_response(
        jsonify(
            message="Lista de tarefas obtida com sucesso",
            tarefas=tarefas
        )
    )

@app.route('/tarefas', methods=['POST'])
def post_tarefas():
    tarefa = request.json
    tarefas.append(tarefa)
    return make_response(
        jsonify(
            message="Tarefa adicionada com sucesso",
            tarefa=tarefa
        )
    )

@app.route('/tarefas', methods=['DELETE'])
def delete_tarefas():
    tarefa_id = request.json.get('id')
    tarefa_titulo = request.json.get('titulo')
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != tarefa_id]
    return make_response(
        jsonify(
            message="Tarefa removida com sucesso",
            id=tarefa_id,
            titulo=tarefa_titulo
        )
    )

if __name__ == '__main__':
    app.run()