import os
import pytest
import sqlite3
import tempfile

from twit_app import create_app, db

pytest.TEST_DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'test.sqlite3') 

@pytest.fixture(autouse=True, scope="session")
def config_setup():
    f = open(pytest.TEST_DB_FILEPATH, 'wb')
    yield
    os.remove(pytest.TEST_DB_FILEPATH)
    pytest.TEST_DB_FILEPATH = None

@pytest.fixture(autouse=True, scope="session")
def app():
    config = {
        'SQLALCHEMY_DATABASE_URI' : f"sqlite:///{pytest.TEST_DB_FILEPATH}",
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }
    return create_app(config)

@pytest.fixture
def create_conn():
    conn = sqlite3.connect(pytest.TEST_DB_FILEPATH)
    yield conn
    conn.close()

@pytest.fixture
def db_session():
    yield db

@pytest.fixture(autouse=True, scope="function")
def config_db(client):
    db.drop_all()
    db.create_all()

