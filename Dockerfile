# Указываем базовый образ
FROM python:3.12-slim

# Условия работы
WORKDIR /app

# Обновляем pip
RUN pip install --upgrade pip

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем необходимые пакеты
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Запуск приложения Django
CMD ["python", "buildingsite/manage.py", "runserver", "0.0.0.0:8000"]