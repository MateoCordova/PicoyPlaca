from App.app import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_canDrive(client):
    response = client.get('/plate/canDrive/?plate=PTQ0601&date=30-05-2022&hour=22%3A37')
    assert response.data == b'{\n  "canDrive": true, \n  "date": "30-05-2022", \n  "plate": "PTQ0601", \n  "time": "22:37"\n}\n'
    response = client.get('/plate/canDrive/?plate=PTQ0601&date=30-05-2022&hour=20%3A15')
    assert response.data == b'{\n  "canDrive": false, \n  "date": "30-05-2022", \n  "plate": "PTQ0601", \n  "time": "20:15"\n}\n'
    response = client.get('/plate/canDrive/?plate=PTQPPP1&date=30-05-2022&hour=22%3A37')
    assert response.status_code == 400
    response = client.get('/plate/canDrive/?plate=PTQ0601&date=31-02-2022&hour=22%3A37')
    assert response.status_code == 400
    response = client.get('/plate/canDrive/?plate=PTQ0601&date=30-05-2022&hour=29%3A00')
    assert response.status_code == 400

