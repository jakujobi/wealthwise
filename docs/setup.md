# Setup Instructions

Follow these steps to set up the WealthWise project locally:

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- PostgreSQL
- Git

## Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jakujobi/wealthwise.git
   cd wealthwise
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Create a PostgreSQL database and user:
     ```sql
     CREATE DATABASE wealthwise_db;
     CREATE USER wealthwise_user WITH PASSWORD 'securepassword';
     ALTER ROLE wealthwise_user SET client_encoding TO 'utf8';
     ALTER ROLE wealthwise_user SET default_transaction_isolation TO 'read committed';
     ALTER ROLE wealthwise_user SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE wealthwise_db TO wealthwise_user;
     ```

   - Update the `DATABASES` settings in `core/settings.py` if necessary.

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser account:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open your web browser and navigate to `http://localhost:8000/`.

## Additional Configuration

- **Static Files:**
  Ensure that the `STATIC_URL` and `STATICFILES_DIRS` settings in `core/settings.py` are correctly configured for serving static files.

- **Media Files:**
  Ensure that the `MEDIA_URL` and `MEDIA_ROOT` settings in `core/settings.py` are correctly configured for serving media files.

- **Environment Variables:**
  Set the following environment variables for sensitive information:
  - `DJANGO_SECRET_KEY`
  - `DATABASE_NAME`
  - `DATABASE_USER`
  - `DATABASE_PASSWORD`
  - `DATABASE_HOST`
  - `DATABASE_PORT`

For more detailed setup instructions, refer to the [official Django documentation](https://docs.djangoproject.com/en/stable/).
