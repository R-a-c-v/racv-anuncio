from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

dbt = SQLAlchemy()
migrate = Migrate()
#123


def create_app(config_mode='development'):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_mode])    
   
    dbt.init_app(app)
    migrate.init_app(app, dbt)

    return app
