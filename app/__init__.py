from flask import Flask, request, jsonify 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
import os

dbt = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_mode])    
 
    dbt.init_app(app)
    migrate.init_app(app, dbt)
    
    from app.anuncios.routes.urls import bp as collector_bp
    app.register_blueprint(collector_bp)          # no prefix → /ping
    

    return app
