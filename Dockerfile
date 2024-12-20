FROM python:3
COPY app/ /app/
ENTRYPOINT ["python3", "/app/main.py"]