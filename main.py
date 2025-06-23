from flask import Flask, make_response, jsonify, request
from dotenv import load_dotenv
load_dotenv()
from db import db
from config import Config
from models import Tarefa
from collections import OrderedDict

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.config['JSON_SORT_KEYS'] = False

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = Tarefa.query.all()
    lista_tarefas = []
    for tarefa in tarefas:
        lista_tarefas.append(OrderedDict({
            'cod_id': tarefa.cod_id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status,
            'data_criacao': tarefa.data_criacao.strftime('%Y-%m-%d %H:%M:%S') if tarefa.data_criacao else None
        }))
    return make_response(jsonify(
        message="Lista de tarefas obtida com sucesso",
        tarefas=lista_tarefas
    ))

@app.route('/tarefas', methods=['POST'])
def post_tarefas():
    dados = request.json
    nova_tarefa = Tarefa(
        titulo=dados.get('titulo'),
        descricao=dados.get('descricao'),
        status=dados.get('status', False)
    )
    db.session.add(nova_tarefa)
    db.session.commit()

    tarefa_ordenada = OrderedDict([
        ('cod_id', nova_tarefa.cod_id),
        ('titulo', nova_tarefa.titulo),
        ('descricao', nova_tarefa.descricao),
        ('status', nova_tarefa.status),
        ('data_criacao', nova_tarefa.data_criacao.strftime('%Y-%m-%d %H:%M:%S'))
    ])

    return make_response(jsonify(
        message="Tarefa adicionada com sucesso",
        tarefa=tarefa_ordenada
    ))

@app.route('/tarefas', methods=['PUT'])
def update_tarefa():
    dados = request.json
    tarefa_id = dados.get('cod_id')

    tarefa = Tarefa.query.get(tarefa_id)

    if tarefa:
        # Atualizar campos se forem enviados
        if 'titulo' in dados:
            tarefa.titulo = dados['titulo']
        if 'descricao' in dados:
            tarefa.descricao = dados['descricao']

        db.session.commit()

        tarefa_atualizada = OrderedDict([
            ('cod_id', tarefa.cod_id),
            ('titulo', tarefa.titulo),
            ('descricao', tarefa.descricao),
            ('status', tarefa.status),
            ('data_criacao', tarefa.data_criacao.strftime('%Y-%m-%d %H:%M:%S'))
        ])

        return make_response(jsonify(
            message="Tarefa atualizada com sucesso",
            tarefa=tarefa_atualizada
        ))
    else:
        return make_response(jsonify(
            message="Tarefa não encontrada",
            cod_id=tarefa_id
        ), 404)

@app.route('/tarefas', methods=['DELETE'])
def delete_tarefas():
    tarefa_id = request.json.get('cod_id')
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return make_response(jsonify(
            message="Tarefa removida com sucesso",
            cod_id=tarefa_id
        ))
    else:
        return make_response(jsonify(
            message="Tarefa não encontrada",
            cod_id=tarefa_id
        ), 404)

if __name__ == '__main__':
    with app.app_context():
        # NÃO rodar create_all pra não recriar a tabela
        pass
    app.run(debug=False)
