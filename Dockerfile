FROM python:3.11-slim

WORKDIR /app


# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=1000  -r requirements.txt

# Копируем код
COPY main.py .
COPY templates templates/
COPY static static/

# Открываем порт
EXPOSE 5000

# Команда запуска
CMD ["python", "main.py"]