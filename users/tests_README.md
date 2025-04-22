# Unit & Integration Test Documentation (White‑Box) for Users App

This document describes comprehensive white-box testing for the WealthWise user registration and login workflows. These tests validate the internal implementation details of the Django forms, views, and authentication mechanisms by directly interacting with application code and database models.

---

## Environment

- **Django Settings Module**: `core.settings`  
- **Test Framework**: Django `TestCase`, configured via `pytest.ini`  
- **Test Client**: `django.test.Client`  
- **Test Log**: `users/user_tests.log`  
- **Django Version**: 5.1.5
- **Python Version**: 3.10+
- **Database**: PostgreSQL (test database created automatically)

---

## How Tests Were Run

### Prerequisites
- Virtual environment activated: `.\wealth.venv\Scripts\Activate.ps1`
- Dependencies installed: `pip install -r requirements.txt`
- PostgreSQL service running
- Database user with CREATE DATABASE permissions

### Test Execution
The unit and integration tests were executed using Django's built-in test runner with the following command:

```bash
python manage.py test users --verbosity=2 2>&1 | tee user_tests.log
```

This command:
1. Creates a dedicated test database (`test_wealthwise_db`)
2. Runs database migrations in the test environment
3. Executes all test methods in the `users/tests.py` file
4. Sets verbosity level to 2 for detailed output
5. Pipes output to both console and the `user_tests.log` file
6. Destroys the test database after completion

The tests can also be run using pytest:

```bash
pytest users/tests.py -v --ds=core.settings
```

---

## 1. User Registration Tests

| Test Name                                                     | Description                                                                         | Input                                                                                                     | Action                  | Expected Output                                                                                                | Actual Output (from log)                                               | Result |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------ |
| test_register_get_renders_form                                | GET `/users/register/` should render the registration form                          | N/A                                                                                                       | GET `/users/register/`  | 200 OK; template `register.html` rendered; `form` in context as a CustomUserCreationForm instance              | `test_register_get_renders_form ... ok`                                | Pass   |
| test_register_post_valid_creates_user_and_profile_and_logs_in | Valid signup should create a new User & Profile, authenticate, and redirect to home | `username=newuser`, `email=newuser@example.com`, `password1=ComplexPass#123`, `password2=ComplexPass#123` | POST `/users/register/` | New `User` + `Profile` exist; user is logged in; redirect to `home`; Profile.email matches submitted email     | `test_register_post_valid_creates_user_and_profile_and_logs_in ... ok` | Pass   |
| test_register_post_username_already_exists_shows_error        | Submitting a duplicate username should return a username‑taken error                | `username=dup` (pre‑created), valid `email`, matching passwords                                           | POST `/users/register/` | Form error on `username`: "A user with that username already exists."; status 200; form re-rendered with error | `test_register_post_username_already_exists_shows_error ... ok`        | Pass   |
| test_register_post_passwords_do_not_match                     | Submitting mismatched passwords should return a password‑mismatch error             | `username=user2`, `email=u2@example.com`, `password1=ComplexPass#123`, `password2=DifferentPass#456`      | POST `/users/register/` | Form error on `password2`: "The two password fields didn't match."; status 200; form re-rendered with error    | `test_register_post_passwords_do_not_match ... ok`                     | Pass   |
| test_register_post_invalid_email                              | Submitting an invalid email should return an invalid‑email error                    | `username=user3`, `email=not-an-email`, matching valid passwords                                          | POST `/users/register/` | Form error on `email`: "Enter a valid email address."; status 200; form re-rendered with error                 | `test_register_post_invalid_email ... ok`                              | Pass   |

---

## 2. User Login Tests

| Test Name                                          | Description                                                            | Input                                        | Action               | Expected Output                                                                                                | Actual Output (from log)                                    | Result |
| -------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------ |
| test_login_get_renders_form                        | GET `/users/login/` should render the login form                       | N/A                                          | GET `/users/login/`  | 200 OK; template `login.html` rendered; `form` in context as an AuthenticationForm instance                    | `test_login_get_renders_form ... ok`                        | Pass   |
| test_login_post_valid_credentials                  | Submitting valid credentials should authenticate and redirect to home  | `username=loginuser`, `password=LoginPass#1` | POST `/users/login/` | User authenticated; redirect to `home`; request.user.is_authenticated is True after redirect                   | `test_login_post_valid_credentials ... ok`                  | Pass   |
| test_login_post_invalid_password_shows_error       | Submitting a wrong password should return non‑field error              | `username=baduser`, `password=WrongPass#1`   | POST `/users/login/` | Non‑field form error: "Please enter a correct username and password."; status 200; form re-rendered with error | `test_login_post_invalid_password_shows_error ... ok`       | Pass   |
| test_login_post_nonexistent_user_shows_error       | Submitting a username that doesn't exist should return non‑field error | `username=noexist`, `password=Whatever#1`    | POST `/users/login/` | Non‑field form error: "Please enter a correct username and password."; status 200; form re-rendered with error | `test_login_post_nonexistent_user_shows_error ... ok`       | Pass   |
| test_login_post_blank_fields_shows_required_errors | Leaving credentials blank should return required‑field errors          | `username=`, `password=`                     | POST `/users/login/` | Field‑level errors: "This field is required." on both `username` and `password`; status 200; form re-rendered  | `test_login_post_blank_fields_shows_required_errors ... ok` | Pass   |

---

## 3. White-Box Testing Approach

These tests follow a white-box methodology, meaning:

1. **Form Validation Testing**: Tests directly verify the backend form validation logic in both the CustomUserCreationForm and AuthenticationForm classes.

2. **View Implementation Testing**: Tests verify the view logic that handles form processing, user creation, profile creation, authentication, and redirects.

3. **Database Integration**: Tests confirm that database operations (user/profile creation) work correctly and constraints (like unique username) are enforced.

4. **Authentication System**: Tests verify the Django authentication system properly recognizes valid credentials and rejects invalid ones.

5. **Edge Cases**: Tests include boundary conditions like empty fields, malformed data, and duplicate entries.

This approach provides higher confidence in implementation correctness compared to black-box testing alone.

---

## 4. Test Log Reference

Full feedback from the test run is available in:

