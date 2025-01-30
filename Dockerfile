# 1. Use an official Python image
FROM python:3.10

# 2. Create app directory
WORKDIR /app

# 3. Copy project files into the container
COPY . .

# 4. Install system dependencies (for Postgres connectivity)
RUN apt-get update && apt-get install -y netcat

# 5. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Expose the Django port
EXPOSE 8000

# 7. Default command to run migrations then start Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]