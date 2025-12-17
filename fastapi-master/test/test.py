from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert 'Samarth' in data['message']


def test_statistical_overview():
    response = client.get('/stats/overview')
    assert response.status_code == 200
    assert 'datasets' in response.json()


def test_cars_statistics():
    response = client.get('/stats/cars')
    assert response.status_code == 200
    data = response.json()
    assert 'total_cars' in data
    assert 'fuel_distribution' in data


def test_correlation_analysis():
    response = client.get('/analysis/correlation')
    assert response.status_code == 200
    assert 'correlation_matrix' in response.json()


def test_distribution_analysis():
    response = client.get('/analysis/distribution/fuel')
    assert response.status_code == 200
    data = response.json()
    assert 'field' in data
    assert 'distribution' in data


def test_filter_cars():
    response = client.get('/data/cars/filter?fuel=electric')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_user():
    response = client.get('/user')
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_read_question():
    response = client.get('/question/1')
    assert response.status_code == 200
    assert response.json()['position'] == 1


def test_read_question_invalid():
    response = client.get('/question/0')
    assert response.status_code == 400
    assert response.json() == {'detail': 'Error'}


def test_read_alternatives():
    response = client.get('/alternatives/1')
    assert response.status_code == 200
    assert response.json()[1]['question_id'] == 1


def test_create_answer():
    body = {"user_id": 1, "answers": [{"question_id": 1, "alternative_id": 2}, {
        "question_id": 2, "alternative_id": 2}, {"question_id": 2, "alternative_id": 2}]}
    body = json.dumps(body)
    response = client.post('/answer', data=body)
    assert response.status_code == 201


def test_read_result():
    response = client.get('/result/1')
    assert response.status_code == 200
