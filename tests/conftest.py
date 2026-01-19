import pytest
from app import create_app,dbt

@pytest.fixture
def app():
    app = create_app("development")
  
    with app.app_context():
        dbt.create_all()
        yield app
        dbt.drop_all()

