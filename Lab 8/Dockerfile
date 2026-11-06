FROM python:3.11-slim

WORKDIR /app

COPY *.py .
COPY classes/ ./classes/
COPY inventory.json .

CMD ["python", "main.py"]
