
import os
import tempfile
import pytest

from application.app import app

#TODO: Move to FlaskTest

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])


def test_get_wine_empty(client):
    r = client.get("/wines")
    assert '' in r.data

def test_get_all_wine(client):
    pass