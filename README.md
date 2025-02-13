# WealthWise
Project for SE 306

Server starts on
http://localhost:8000/

# (most of these are run automaticly)
# Command for running the server

## create app
python manage.py startapp [app name]

## run dev server
python manage.py runserver

## create databases for libraries
python manage.py migrate

## create file to make models for database
python manage.py makemigrations [app name]

## create admin user
python manage.py createsuperuser

## In order to auto install required python Libraries
pip install -r requirements.txt