# WealthWise Testing Documentation

## Overview
This directory contains the test suite for the WealthWise application. The test suite uses both pytest and Django's built-in testing framework to provide comprehensive testing coverage for all components of the application.

## Test Structure
```
tests/
├── __init__.py
├── conftest.py          # Shared pytest fixtures
├── settings.py          # Test-specific Django settings
├── README.md           # This file
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
- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test interactions between components
- **View Tests**: Test HTTP responses and context
- **Model Tests**: Test model validation and methods
- **Form Tests**: Test form validation and processing
- **API Tests**: Test REST endpoints
- **Selenium Tests**: Test browser interactions

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
The following markers are available for categorizing tests:
- `@pytest.mark.unit`: Unit tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.views`: View tests
- `@pytest.mark.models`: Model tests
- `@pytest.mark.forms`: Form tests
- `@pytest.mark.slow`: Slow tests (can be skipped with -m "not slow")
- `@pytest.mark.api`: API tests
- `@pytest.mark.selenium`: Browser automation tests

## Test Data Factories
We use Factory Boy for generating test data. Factories are available for all major models:

```python
# Example usage
from tests.users.factories import UserFactory
from tests.calculators.factories import FinancialToolUsageFactory
from tests.schedule.factories import ConsultationFactory, EventFactory

# Create a single instance
user = UserFactory()
tool_usage = FinancialToolUsageFactory()

# Create multiple instances
users = UserFactory.create_batch(size=3)
events = EventFactory.create_batch(size=5)
```

## Configuration Files

### pytest.ini
- Configures Django settings module
- Sets up coverage reporting
- Defines test markers
- Configures test discovery patterns
- Sets warning filters

### .coveragerc
- Configures coverage measurement
- Excludes irrelevant files
- Sets up coverage reporting options
- Defines source directories to measure

### tests/settings.py
- Uses in-memory SQLite database
- Disables migrations during testing
- Uses faster password hasher
- Disables logging
- Uses local memory cache
- Disables CSRF for testing

## Writing Tests

### Example: Model Test
```python
@pytest.mark.django_db
class TestFinancialToolUsage:
    def test_financial_tool_usage_creation(self):
        tool_usage = FinancialToolUsageFactory()
        assert tool_usage.usage_id is not None
        assert tool_usage.tool_type in ['budget', 'compound_interest', 'retirement']
```

### Example: View Test
```python
@pytest.mark.django_db
class TestCalculatorViews:
    def test_budget_calculator_view(self, client, test_user):
        client.login(username='testuser', password='testpass123')
        url = reverse('budget-calculator')
        response = client.get(url)
        assert response.status_code == 200
```

### Example: Form Test
```python
class TestScheduleForms:
    def test_valid_consultation_form(self):
        advisor = UserFactory()
        form_data = {
            'advisor_id': advisor.id,
            'scheduled_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'scheduled'
        }
        form = ConsultationForm(data=form_data)
        assert form.is_valid()
```

## Best Practices

1. **Test Organization**
   - Keep tests close to the code they're testing
   - Use clear, descriptive test names
   - Group related tests in classes
   - Use appropriate markers

2. **Test Data**
   - Use factories instead of direct model creation
   - Don't rely on database state between tests
   - Clean up after tests when necessary
   - Use realistic test data

3. **Assertions**
   - Test one thing per test method
   - Use descriptive assertion messages
   - Check both positive and negative cases
   - Verify side effects when appropriate

4. **Performance**
   - Use `--reuse-db` to speed up test runs
   - Mark slow tests with `@pytest.mark.slow`
   - Use in-memory database for testing
   - Minimize database queries in tests

5. **Coverage**
   - Aim for high test coverage
   - Focus on critical paths
   - Don't just test happy paths
   - Test edge cases and error conditions

## Continuous Integration

The test suite is configured to run in CI environments. Key features:
- Automatic test runs on pull requests
- Coverage reporting
- Test result reporting
- Performance metrics

## Troubleshooting

Common issues and solutions:

1. **Database Issues**
   ```bash
   # Reset test database
   pytest --create-db
   ```

2. **Fixture Issues**
   ```bash
   # Show available fixtures
   pytest --fixtures
   ```

3. **Coverage Issues**
   ```bash
   # Clear coverage data
   coverage erase
   ```

4. **Debugging Tests**
   ```bash
   # Run with increased verbosity
   pytest -vv
   
   # Run specific test with print statements
   pytest path/to/test.py::TestClass::test_name -s
   ``` 