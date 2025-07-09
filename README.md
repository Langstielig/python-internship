# python-internship

### Создание виртуального окружения:
python -m venv venv

### Запуск виртуального окружения:
.\venv\Scripts\Activate.ps1

### Установка библиотек:
pip install -r .\requirements.txt

### Загрузка модели:
python3 download_models.py

# 1 Вариант

### Запуск fastapi сервиса
uvicorn fast_api_app:app --reload

### Открыть приложение по следующей ссылке
http://127.0.0.1:8000/docs

# 2 Вариант

### Создание Docker образа:
docker image build . --tag fast_api:with_volume

### Запуск приложения внутри Docker контейнера:
docker container run --publish 4600:1702 -v ./models:/project/models -v ./logs:/project/logs fast_api:with_volume

### Открыть приложение по следующей ссылке:
http://localhost:4600/docs
