from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
import os
print("SQLALCHEMY_DATABASE_URI =", os.getenv("SQLALCHEMY_DATABASE_URI"))
dbt = SQLAlchemy()
migrate = Migrate()
#123


def create_app(config_mode):
 

    app = Flask(__name__)
    CORS(app)
    
    if config_mode == "testing":
        app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )  

    app.config.from_object(config[config_mode])    
    



    dbt.init_app(app)
    migrate.init_app(app, dbt)

    return app
