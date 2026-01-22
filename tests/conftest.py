import pytest
from app import create_app, dbt

@pytest.fixture
def app():
    app = create_app("testing")
    app.config.update({"TESTING": True})
    with app.app_context():
        dbt.create_all()  # cria as tabelas em memória
        yield app
        dbt.drop_all()    # limpa depois do teste

@pytest.fixture
def client(app):
    return app.test_client()
