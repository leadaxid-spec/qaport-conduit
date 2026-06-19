# mock_backend/main.py
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Conduit Mock API")

class UserData(BaseModel):
    username: str
    email: str
    password: str

class RegisterRequest(BaseModel):
    user: UserData

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def register_user(payload: RegisterRequest):
    return {
        "user": {
            "email": payload.user.email,
            "username": payload.user.username,
            "token": f"mock-jwt-token-{payload.user.username}-xyz"
        }
    }

@app.get("/api/articles")
def get_articles():
    return {
        "articles": [],
        "articlesCount": 0
    }