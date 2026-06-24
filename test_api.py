import pytest
import requests
import uuid

@pytest.fixture(scope="session")
def user_token() -> str:
    """Фикстура регистрирует уникального пользователя и возвращает его токен."""
    unique_id = uuid.uuid4().hex
    
    payload = {
        "user": {
            "username": f"user_{unique_id}",
            "email": f"api_{unique_id}@example.com",
            "password": "Secret_Password_123"
        }
    }
    
    response = requests.post("http://localhost:3000/api/users", json=payload)
    
    assert response.status_code == 201, f"Неверный статус-код! Ответ сервера: {response.text}"
    
    token = response.json()["user"]["token"]
    return token


def test_user_authentication_contract(user_token: str):
    assert user_token, "Получен пустой токен от бэкенда"
    
    assert user_token.startswith("mock-jwt-token-"), f"Токен имеет неверный формат: {user_token}"
    
    print(f"\n[INFO] Контракт API проверен успешно. Токен: {user_token}")