FROM python:3.11-slim
COPY . ./project
WORKDIR /project
RUN pip3 install -r requirements.txt
EXPOSE 1702
VOLUME ["/models", "/logs"]
CMD ["uvicorn", "fast_api_app:app", "--reload", "--port", "1702", "--host", "0.0.0.0"]