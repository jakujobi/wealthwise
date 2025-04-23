# Project Overview

## Introduction

WealthWise is a comprehensive financial management and education platform designed to help users make informed financial decisions. The platform includes financial calculators, scheduling tools for financial consultations, educational resources, and user account management.

## Project Goals

WealthWise aims to:

1. Provide accurate and user-friendly financial calculation tools
2. Connect users with financial advisors through consultation scheduling
3. Educate users about financial concepts and strategies
4. Offer personalized financial insights based on user data
5. Ensure security and privacy for sensitive financial information

## Architecture

WealthWise follows a standard Django MVT (Model-View-Template) architecture:

- **Models**: Database schemas defined in each app's `models.py`
- **Views**: Business logic and request handling in each app's `views.py`
- **Templates**: HTML templates in each app's `templates/` directory

### High-Level Architecture

```
+-----------------+      +------------------+      +------------------+
|                 |      |                  |      |                  |
|  Web Browser    +----->+  Django App      +----->+  PostgreSQL DB   |
|                 |      |                  |      |                  |
+-----------------+      +------------------+      +------------------+
                                 |
                                 |
                                 v
                         +------------------+
                         |                  |
                         |  Static Assets   |
                         |  (CSS, JS, etc.) |
                         |                  |
                         +------------------+
```

## Technology Stack

### Backend
- **Python 3.x**: Primary programming language
- **Django 4.x**: Web framework
- **Django REST Framework**: API development
- **PostgreSQL**: Primary database
- **Gunicorn**: WSGI HTTP Server

### Frontend
- **HTML5/CSS3**: Markup and styling
- **JavaScript**: Client-side logic
- **Bootstrap**: CSS framework for responsive design

### Testing
- **pytest**: Testing framework
- **Factory Boy**: Test data generation
- **Coverage.py**: Code coverage measurement

### Deployment
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Nginx**: Web server

## Project Structure

WealthWise is organized into several Django apps, each responsible for a specific area of functionality:

- **Users**: User account management, authentication, and profiles
- **Calculators**: Financial calculation tools
- **Schedule**: Consultation and event scheduling
- **Learning**: Educational content and resources
- **Core**: Core settings and configuration

## Data Flow

1. User authenticates through the Users app
2. Authenticated users can access:
   - Financial calculators to perform calculations
   - Schedule consultations with advisors
   - View educational content
   - Manage their profile information
3. All user actions are logged and can be used for personalized insights

## Development Workflow

The development workflow follows these steps:

1. Feature planning and documentation
2. Development in feature branches
3. Testing using the comprehensive test suite
4. Code review and quality assurance
5. Merging to main branch
6. Deployment through the CI/CD pipeline

## Next Steps

- [Getting Started](./getting-started.md) - Setup your development environment
- [Application Structure](./application-structure.md) - Understand the codebase organization
- [Database Schema](./database-schema.md) - Learn about the data models 