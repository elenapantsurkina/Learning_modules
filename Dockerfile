# Используем официальный slim-образ Python 3.12
FROM python:3.12-slim


# Устанавливаем рабочую директорию в контейнере
WORKDIR /app


# Устанавливаем необходимые системные зависимости
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы проекта в контейнер
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости проекта
RUN poetry install --no-root -vvv

# Копируем исходный код приложения в контейнер
COPY . .

# Определяем переменные окружения
ENV SECRET_KEY="django-insecure-6be+fa)7ed_w2!+38-2z8md3l@*#3-n***un0^qeeop99qo#ek"
ENV CELERY_BROKER_URL="redis://127.0.0.1:6379/0"
ENV CELERY_BACKEND="redis://127.0.0.1:6379/0"

# Пробрасываем порт, который будет использовать Django
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
