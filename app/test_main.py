from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

#тест проверяет, что на вход функции передан валидный массив и функция отдала отсортированный массив
def test_sort_array():
    response = client.post('/sort',data = '{"myKey": [9,7,4,1]}')
    assert response.status_code == 200
    assert response.json().get('myKey',[]) == [1,4,7,9]