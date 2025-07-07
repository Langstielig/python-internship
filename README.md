# python-internship

### Загрузка модели:
python3 download_models.py

### Создание Docker образа:
docker image build . --tag fast_api:with_volume

### Запуск приложения внутри Docker контейнера:
docker container run --publish 4600:1702 -v ./models:/project/models -v ./logs:/project/logs fast_api:with_volume

### Открыть приложение по следующей ссылке:
http://localhost:4600/docs
