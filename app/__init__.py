from flask import Flask
from .config import Config
from .db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)

    from .routes import tarefas_bp
    app.register_blueprint(tarefas_bp)

    return app
