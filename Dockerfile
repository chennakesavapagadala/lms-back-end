# Dockerfile

FROM python:3.11-slim

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY . .

CMD ["gunicorn", "lms_project.wsgi:application", "--bind", "0.0.0.0:8000"]


