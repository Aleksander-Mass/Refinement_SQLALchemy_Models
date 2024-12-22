from fastapi import FastAPI
from app.routers import task, user

# Создание приложения FastAPI
app = FastAPI()

# Основной маршрут

@app.get("/")
def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключение маршрутов
app.include_router(task.router)
app.include_router(user.router)