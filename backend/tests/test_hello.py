from app import APP


def test_hello():
    response = APP.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello World!'
