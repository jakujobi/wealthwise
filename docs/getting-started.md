# Getting Started

This guide will help you set up your development environment and understand the basics of contributing to the WealthWise project.

## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.8 or higher
- PostgreSQL 12 or higher
- Docker and Docker Compose (optional, for containerized development)
- Git

## Development Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/wealthwise.git
cd wealthwise
```

### 2. Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv wealth.venv

# Activate the virtual environment
# On Windows
wealth.venv\Scripts\activate
# On macOS/Linux
source wealth.venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgres://username:password@localhost:5432/wealthwise
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Set Up the Database

```bash
# Create the database
createdb wealthwise

# Run migrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000/`.

## Docker Setup (Alternative)

If you prefer to use Docker for development:

```bash
# Build and start containers
docker-compose up -d

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

The server will be available at `http://localhost:8000/`.

## Project Commands

Here are some useful commands for development:

```bash
# Run the development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run tests
pytest

# Run tests with coverage
pytest --cov

# Collect static files
python manage.py collectstatic

# Create a new app
python manage.py startapp appname
```

## Development Workflow

1. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**

   - Write code
   - Add tests
   - Update documentation

3. **Run Tests**

   ```bash
   pytest
   ```

4. **Check Code Coverage**

   ```bash
   pytest --cov
   ```

5. **Commit Your Changes**

   ```bash
   git add .
   git commit -m "Description of changes"
   ```

6. **Push to GitHub**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**

   - Go to the repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Add a description of your changes
   - Submit the pull request

## Code Style Guidelines

We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code. Some key points:

- Use 4 spaces for indentation
- Maximum line length of 79 characters
- Use descriptive variable names
- Add docstrings to all functions, classes, and modules
- Include type hints where appropriate

## Directory Structure

```
wealthwise/
├── calculators/         # Financial calculators app
├── core/                # Core settings and configuration
├── docs/                # Documentation
├── learning/            # Educational content app
├── media/               # User-uploaded files
├── schedule/            # Consultation scheduling app
├── static/              # Static files (CSS, JS, images)
├── templates/           # Project-wide templates
├── tests/               # Test suite
├── users/               # User management app
├── .env                 # Environment variables (not in repository)
├── .gitignore           # Git ignore file
├── docker-compose.yml   # Docker Compose configuration
├── Dockerfile           # Docker configuration
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Next Steps

- [Application Structure](./application-structure.md) - Learn about the codebase structure
- [Database Schema](./database-schema.md) - Understand the data models
- [User Module](./user-module.md) - Explore the user management functionality 