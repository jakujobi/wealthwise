FROM python:3.10

WORKDIR /app

COPY . .

# Explicitly install netcat-openbsd:
RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
