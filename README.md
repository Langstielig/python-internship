# python-internship

Установка Python3.10

- brew install python@3.10

Создание виртуального окружения

- python3.10 -m venv .venv_assistant

Запуск виртуального окружения

- source .venv_assistant/bin/activate

Установка библиотек

- pip install -r requirements.txt

Для загрузки моделей нужно выполнить команду

- python3 download_model.py

Запуск fastapi сервиса

- uvicorn assistant_service.main:app --reload
