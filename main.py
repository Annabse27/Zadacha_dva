from fastapi import FastAPI, HTTPException

# Инициализация FastAPI приложения
app = FastAPI()

# 📋 Данные о работниках
workers = [
    {"ID": 1, "ФИО": "Иванов", "Номер бригады": 1, "ЗП": 10000, "Специализация": "Черновая отделка"},
    {"ID": 2, "ФИО": "Петров", "Номер бригады": 2, "ЗП": 12000, "Специализация": "Чистовая отделка"},
    {"ID": 3, "ФИО": "Сидоров", "Номер бригады": 1, "ЗП": 16000, "Специализация": "Бригадир"},
    {"ID": 4, "ФИО": "Сергеев", "Номер бригады": 1, "ЗП": 20000, "Специализация": "Прораб"},
    {"ID": 5, "ФИО": "Сергеев", "Номер бригады": 2, "ЗП": 20000, "Специализация": "Прораб"},
]

# 📍 Эндпоинт 1: Получить список работников по номеру бригады
@app.get("/api/v1/team/{team_id}/WorkerList")
def get_team_workers(team_id: int):
    """
    Эндпоинт возвращает список работников, которые принадлежат к определённой бригаде.
    :param team_id: Номер бригады
    :return: Список работников бригады или ошибка 404, если бригада не найдена
    """
    team_workers = [worker for worker in workers if worker["Номер бригады"] == team_id]
    if not team_workers:
        raise HTTPException(status_code=404, detail=f"Бригада с номером {team_id} не найдена")
    return {"Номер бригады": team_id, "Работники": team_workers}


# 📍 Эндпоинт 2: Получить описание конкретного работника по его ID
@app.get("/api/v1/worker/{worker_id}")
def get_worker(worker_id: int):
    """
    Эндпоинт возвращает информацию о конкретном работнике по его ID.
    :param worker_id: ID работника
    :return: Информация о работнике или ошибка 404, если работник не найден
    """
    worker = next((worker for worker in workers if worker["ID"] == worker_id), None)
    if not worker:
        raise HTTPException(status_code=404, detail=f"Работник с ID {worker_id} не найден")
    return worker


# 📍 Эндпоинт 3 (опционально): Получить список всех работников
@app.get("/api/v1/workers")
def get_all_workers():
    """
    Эндпоинт возвращает полный список всех работников.
    :return: Список всех работников
    """
    return {"Работники": workers}
