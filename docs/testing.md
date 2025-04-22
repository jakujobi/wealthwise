# Testing

This document provides an overview of the testing strategy and infrastructure for the WealthWise application.

## Testing Philosophy

WealthWise follows a comprehensive testing approach with these core principles:

1. **Test-driven development**: Write tests before implementing features
2. **High test coverage**: Aim for 90%+ code coverage
3. **Multiple test types**: Unit, integration, and end-to-end tests
4. **Automation**: Automated testing in CI/CD pipeline
5. **Realistic data**: Use factories to generate test data that reflects real-world usage

## Testing Stack

WealthWise uses the following testing tools:

- **pytest**: Primary testing framework
- **Django's TestCase**: For Django-specific functionality
- **Factory Boy**: For test data generation
- **Coverage.py**: For code coverage reporting
- **Selenium**: For browser-based testing (when needed)

## Test Organization

Tests are organized in a dedicated `tests` directory at the project root:

```
tests/
├── __init__.py
├── conftest.py          # Shared pytest fixtures
├── settings.py          # Test-specific Django settings
├── README.md           # Testing documentation
├── users/              # User app tests
│   ├── factories.py    # Test data factories
│   ├── test_models.py  # Model tests
│   ├── test_views.py   # View tests
│   └── test_forms.py   # Form tests
├── calculators/        # Calculator app tests
│   ├── factories.py
│   ├── test_models.py
│   ├── test_views.py
│   └── test_forms.py
├── schedule/          # Schedule app tests
│   ├── factories.py
│   ├── test_models.py
│   ├── test_views.py
│   └── test_forms.py
└── learning/         # Learning app tests
    └── test_views.py
```

## Test Categories

The test suite includes several types of tests:

### Unit Tests

Unit tests verify that individual components work correctly in isolation:

- Model validations and methods
- Form validations and methods
- Utility functions
- View logic

### Integration Tests

Integration tests verify that components work correctly together:

- Views with templates
- Forms with models
- Views with database operations
- API endpoints

### End-to-End Tests

End-to-end tests verify complete user flows:

- User registration and login
- Calculation flows
- Consultation scheduling
- Event registration

## Running Tests

### Basic Commands

```bash
# Run all tests
pytest

# Run tests for a specific app
pytest tests/users/
pytest tests/calculators/
pytest tests/schedule/
pytest tests/learning/

# Run tests by category
pytest -m unit
pytest -m integration
pytest -m views
pytest -m models
pytest -m forms
pytest -m api
pytest -m selenium

# Run tests and generate coverage report
pytest --cov

# View coverage report in browser
python -m http.server --directory htmlcov
```

### Test Markers

The test suite uses pytest markers to categorize tests:

- `@pytest.mark.unit`: Unit tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.views`: View tests
- `@pytest.mark.models`: Model tests
- `@pytest.mark.forms`: Form tests
- `@pytest.mark.slow`: Slow tests (can be skipped with -m "not slow")
- `@pytest.mark.api`: API tests
- `@pytest.mark.selenium`: Browser automation tests

## Test Configuration

### pytest.ini

The `pytest.ini` file in the project root configures pytest:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = tests.settings
python_files = tests.py test_*.py *_tests.py
addopts = 
    --reuse-db 
    --cov=.
    --cov-report=html
    --cov-report=term-missing
    --cov-config=.coveragerc
    -v
testpaths = tests
filterwarnings =
    ignore::DeprecationWarning
    ignore::UserWarning
markers =
    unit: mark a test as a unit test
    integration: mark a test as an integration test
    views: mark a test as a view test
    models: mark a test as a model test
    forms: mark a test as a form test
    slow: marks tests as slow (deselect with '-m "not slow"')
    api: marks tests as API tests
    selenium: marks tests as selenium tests
```

### .coveragerc

The `.coveragerc` file configures code coverage measurement:

```ini
[run]
source = .
omit =
    */migrations/*
    */tests/*
    */venv/*
    */wealth.venv/*
    manage.py
    */wsgi.py
    */asgi.py
    */settings.py
    */urls.py
    */__init__.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    def __str__
    raise NotImplementedError
    if settings.DEBUG
    if __name__ == .__main__.:
    pass
    raise ImportError
    except ImportError
    def main()

[html]
directory = htmlcov
```

### tests/settings.py

The `tests/settings.py` file provides test-specific Django settings:

```python
from core.settings import *

# Use an in-memory SQLite database for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable migrations during testing
MIGRATION_MODULES = {app: None for app in INSTALLED_APPS}

# Use a faster password hasher during tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable logging during tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}
```

## Test Fixtures

Test fixtures are defined in `tests/conftest.py` and app-specific fixture files:

```python
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_client(api_client):
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def test_user():
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
```

## Test Factories

Test factories use Factory Boy to generate test data:

```python
import factory
from django.contrib.auth import get_user_model
from users.models import UserProfile

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')
    is_active = True

class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('text')
```

## Testing Best Practices

### Writing Good Tests

1. **Test One Thing Per Test**: Each test should verify a single behavior
2. **Use Descriptive Test Names**: Name tests to describe what they test
3. **Arrange-Act-Assert**: Structure tests with setup, action, and verification
4. **Don't Test Django**: Don't test framework functionality
5. **Test Edge Cases**: Test boundary conditions and error handling

### Example Test

```python
@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        # Arrange
        username = 'testuser'
        email = 'test@example.com'
        password = 'testpass123'
        
        # Act
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Assert
        assert user.username == username
        assert user.email == email
        assert user.check_password(password)
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
```

## Continuous Integration

Tests are run automatically in the CI/CD pipeline:

1. When pull requests are opened or updated
2. When code is merged to the main branch
3. On a nightly schedule

The CI/CD pipeline:

1. Sets up the test environment
2. Installs dependencies
3. Runs all tests
4. Generates a coverage report
5. Reports test results

## Test Coverage

The project aims for high test coverage:

- 90%+ overall coverage
- 100% for critical functionality
- Coverage reports are generated for every test run

## Troubleshooting

Common testing issues and solutions:

### Database Issues

```bash
# Reset test database
pytest --create-db
```

### Fixture Issues

```bash
# Show available fixtures
pytest --fixtures
```

### Coverage Issues

```bash
# Clear coverage data
coverage erase
```

### Debugging Tests

```bash
# Run with increased verbosity
pytest -vv

# Run specific test with print statements
pytest path/to/test.py::TestClass::test_name -s
```

## Next Steps

- [API Reference](./api-reference.md) - Learn about the REST API
- [Deployment](./deployment.md) - Understand the deployment process
- [Contributing](./contributing.md) - Learn how to contribute to the project 