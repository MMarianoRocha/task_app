from db import db
from datetime import datetime

class Tarefa(db.Model):
    __tablename__ = 'tarefas'  # Nome exato da tabela

    cod_id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(30), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, nullable=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
