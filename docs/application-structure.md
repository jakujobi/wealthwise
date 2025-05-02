# Application Structure

This document explains the organization of the WealthWise codebase and how different components interact with each other.

## Project Structure

WealthWise follows a standard Django project structure, organized by functionality into separate apps. Here's an overview of the main directories:

```
wealthwise/
├── calculators/         # Financial calculators
├── core/                # Core settings and configuration
├── docs/                # Documentation
├── learning/            # Educational resources
├── media/               # User-uploaded files
├── messaging/           # User-to-user messaging system
├── schedule/            # Event and consultation scheduling
├── static/              # Static files (CSS, JS, images)
├── templates/           # Project-wide templates
├── tests/               # Test suite
├── users/               # User management
├── .gitignore           # Git ignore file
├── docker-compose.yml   # Docker Compose configuration
├── Dockerfile           # Docker configuration
├── manage.py            # Django management script
├── pytest.ini           # Pytest configuration
└── requirements.txt     # Python dependencies
```

## Core Components

### Core App

The `core` app contains project-wide settings and configuration:

```
core/
├── __init__.py
├── asgi.py             # ASGI configuration
├── settings.py         # Django settings
├── urls.py             # Project-wide URL routing
├── views.py            # Project-wide views
└── wsgi.py             # WSGI configuration
```

Key functionality:
- Project settings (databases, middleware, installed apps)
- Main URL routing
- Static/media file configuration
- Authentication configuration
- Project-wide utilities

### Users App

The `users` app handles user management, authentication, and profiles:

```
users/
├── __init__.py
├── admin.py            # Django admin configuration
├── apps.py             # App configuration
├── forms.py            # User-related forms
├── migrations/         # Database migrations
├── models.py           # User models
├── templates/          # User-related templates
│   └── users/
│       ├── login.html
│       ├── profile.html
│       └── register.html
├── tests.py            # Tests for users app
├── urls.py             # URL routing for users app
└── views.py            # User-related views
```

Key functionality:
- User registration and authentication
- User profiles and preferences
- Password management
- User roles and permissions

### Calculators App

The `calculators` app provides financial calculation tools:

```
calculators/
├── __init__.py
├── admin.py            # Django admin configuration
├── apps.py             # App configuration
├── migrations/         # Database migrations
├── models.py           # Calculator models
├── templates/          # Calculator templates
│   └── calculators/
│       ├── budget.html
│       ├── compound_interest.html
│       └── retirement.html
├── tests.py            # Tests for calculators app
├── urls.py             # URL routing for calculators app
└── views.py            # Calculator views and logic
```

Key functionality:
- Budget calculations
- Compound interest calculations
- Retirement planning
- Investment returns
- Loan amortization

### Schedule App

The `schedule` app manages events and consultations:

```
schedule/
├── __init__.py
├── admin.py            # Django admin configuration
├── apps.py             # App configuration
├── forms.py            # Schedule-related forms
├── migrations/         # Database migrations
├── models.py           # Schedule models
├── templates/          # Schedule templates
│   └── schedule/
│       ├── consultation_list.html
│       ├── consultation_detail.html
│       ├── event_list.html
│       └── event_detail.html
├── tests.py            # Tests for schedule app
├── urls.py             # URL routing for schedule app
└── views.py            # Schedule views and logic
```

Key functionality:
- Consultation scheduling
- Event management
- Calendar integrations
- Notifications and reminders

### Learning App

The `learning` app provides educational content:

```
learning/
├── __init__.py
├── admin.py            # Django admin configuration
├── apps.py             # App configuration
├── migrations/         # Database migrations
├── models.py           # Learning models
├── templates/          # Learning templates
│   └── learning/
│       ├── home.html
│       ├── resources.html
│       └── article.html
├── tests.py            # Tests for learning app
├── urls.py             # URL routing for learning app
└── views.py            # Learning views and logic
```

Key functionality:
- Educational content delivery
- Financial education resources
- Articles and guides

## Templates

Django templates are organized by app, with project-wide templates in the root `templates` directory:

```
templates/
├── base.html           # Base template with common structure
├── home.html           # Homepage template
├── dashboard.html      # Dashboard template
└── includes/           # Reusable template components
    ├── header.html
    ├── footer.html
    └── navigation.html
```

## Static Files

Static files are organized by type:

```
static/
├── css/                # Stylesheets
├── js/                 # JavaScript files
├── images/             # Images
└── vendors/            # Third-party libraries
```

## URL Structure

WealthWise follows a logical URL structure:

- `/` - Homepage
- `/users/` - User management
  - `/users/login/` - Login
  - `/users/logout/` - Logout
  - `/users/register/` - Registration
  - `/users/profile/` - User profile
- `/calculators/` - Financial calculators
  - `/calculators/budget/` - Budget calculator
  - `/calculators/compound-interest/` - Compound interest calculator
  - `/calculators/retirement/` - Retirement calculator
- `/schedule/` - Schedule management
  - `/schedule/consultations/` - Consultations
  - `/schedule/events/` - Events
- `/learning/` - Educational resources
  - `/learning/resources/` - Learning resources
  - `/learning/articles/` - Articles and guides

## Component Interactions

The apps interact in the following ways:

1. Users app provides authentication for all other apps
2. Calculators app stores calculation history in the database
3. Schedule app references users for consultation scheduling
4. Learning app provides educational content based on user preferences

## Database Access

Each app defines its own models in `models.py`. The main relationships are:

- User profiles are linked to consultation appointments
- User profiles are linked to calculation history
- Consultations are linked to advisors (users with advisor role)
- Events are linked to user profiles

## Next Steps

- [Database Schema](./database-schema.md) - Learn about the data models
- [User Module](./user-module.md) - Explore the user management functionality
- [Calculators Module](./calculators-module.md) - Understand the financial calculators 