from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello"
    }


@app.get("/users")
def users():
    return [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Anna"},
    ]
