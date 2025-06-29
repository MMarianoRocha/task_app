from .db import db
from datetime import datetime
import pytz

fuso_brasil = pytz.timezone('America/Sao_Paulo')
nova_data = datetime.now(fuso_brasil)

class Tarefa(db.Model):
    __tablename__ = 'tarefas'  # Nome exato da tabela

    cod_id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(30), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, nullable=True)
    data_criacao = db.Column(db.DateTime, default=nova_data, nullable=False)
