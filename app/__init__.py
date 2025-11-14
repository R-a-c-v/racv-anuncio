from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

dbt = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    
 
    dbt.init_app(app)
    migrate.init_app(app, dbt)

    # Rota simples para testar
    @app.route('/')
    def home():
        return "Olá Mundo"

    # Rota para receber dados em JSON (POST)
    @app.route('/received-data', methods=['POST'])
    def received_data():
        data = request.get_json()
        return jsonify({
            "message": "Dados recebidos com sucesso!",
            "data": data
        }), 200

    return app
