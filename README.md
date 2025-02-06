# WealthWise
Project for SE 306

# Command for running the server
run dev server
python manage.py runserver

# create app
python manage.py startapp [app name]

# create databases for libraries
python manage.py migrate

# create file to make models for database
python manage.py makemigrations [app name]

# create admin user
python manage.py createsuperuser

# In order to auto install required python Libraries
pip install -r requirements.txt