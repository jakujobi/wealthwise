# WealthWise

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

A comprehensive personal finance management application designed to empower users with tools for budgeting, financial planning, investment tracking, and financial literacy.

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#️-technology-stack)
- [Application Structure](#️-application-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#-usage)
- [Project Documentation](#-project-documentation)
- [Contributing](#-contributing)
- [Developers](#-developers)
- [License](#-license)

## 📋 Overview

WealthWise is a robust financial management platform developed as part of SE 306. The application is designed to provide users with a comprehensive suite of tools to manage their finances effectively, track budgets, plan investments, and improve financial literacy.

## ✨ Features

### 🏠 Core

- **Dashboard**: Personalized financial overview with key metrics and summaries
- **Authentication**: Secure user registration and login system
- **Profile Management**: User profile customization and settings

### 📊 Budgeting & Financial Planning

- **Budget Tool**: Create, track, and manage monthly budgets
- **Expense Tracking**: Log and categorize expenses
- **Income Management**: Record and manage multiple income sources
- **Financial Goals**: Set, track, and achieve financial goals

### 🧮 Financial Calculators

- **Loan Calculator**: Calculate loan payments, interest, and amortization schedules
- **Savings Calculator**: Project savings growth with different interest rates and contribution schedules
- **Investment Calculator**: Estimate investment returns and growth
- **Retirement Calculator**: Plan for retirement with detailed projections


### 📅 Schedule & Reminders

- **Bill Reminders**: Never miss a payment with automated reminders
- **Financial Calendar**: Schedule and track important financial dates
- **Automated Alerts**: Receive notifications for budget overruns, due dates, etc.

### 📚 Learning Hub

- **Financial Articles**: Read curated content on personal finance
- **Tutorial Library**: Access step-by-step guides on using financial tools
- **Resource Center**: Explore additional financial education resources

### 💬 Messaging

- **User-to-User Messaging**: Direct messaging between platform users
- **Conversation Management**: Organize and maintain multiple conversations
- **Read Status Tracking**: Track message read status

## 🛠️ Technology Stack

### Backend

- **Framework**: Django 4.2
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Django Authentication System

### Frontend

- **Template Engine**: Django Templates
- **CSS Framework**: Bootstrap 5
- **JavaScript**: Vanilla JS with some jQuery
- **Icons**: Bootstrap Icons

### Deployment

- **Development**: Django Development Server
- **Production**: Gunicorn + Nginx

## 🏗️ Application Structure

WealthWise follows a modular architecture organized into the following components:

- **core**: Base application with shared templates, static files, and core functionality
- **users**: User authentication, profile management, and user-related models
- **calculators**: Financial calculation tools and algorithms
- **budgeting**: Budget creation, tracking, and analysis tools
- **schedule**: Calendar, reminders, and scheduling functionality
- **learning**: Educational content and resources
- **messaging**: User-to-user communication system

For a detailed breakdown of the application structure, see our [Application Structure Documentation](docs/application-structure.md).

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/username/wealthwise.git
   cd wealthwise
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Setup the database

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin)

   ```bash
   python manage.py createsuperuser
   ```

### Running the Application

1. Start the development server

   ```bash
   python manage.py runserver
   ```

2. Access the application at [http://localhost:8000/](http://localhost:8000/)

3. Access the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 📖 Usage

### Account Setup

1. Register a new account or log in with existing credentials
2. Complete your profile with personal and financial information
3. Configure notification preferences

### Budget Management

1. Create a new budget by selecting "Budgeting" from the navigation
2. Set income sources, expense categories, and saving goals
3. Track spending against your budget throughout the month
4. Review and analyze past budgets

### Financial Calculators

1. Navigate to the "Calculators" section
2. Choose the calculator that fits your needs
3. Enter the required information
4. View and interpret the results

### Learning Resources

1. Visit the "Learning Hub" to access educational content
2. Browse articles by category or search for specific topics
3. Track your learning progress

### Messaging

1. Access the "Messages" feature from the navigation bar
2. Start a new conversation by clicking the "New Message" button
3. Select a recipient from the user list
4. Compose and send your message
5. View and reply to conversations in the messaging interface

## 📚 Project Documentation

Detailed documentation is available in the `docs/` directory:

- [Application Structure](docs/application-structure.md)
- [Database Schema](docs/database-schema.md)
- [API Documentation](docs/api-documentation.md)
- [User Guide](docs/user-guide.md)
- [Messaging Module](docs/messaging-module.md)

### External Documentation

For more extensive documentation, visit our [WealthWise DeepWiki](https://deepwiki.com/jakujobi/wealthwise) repository.

## 🤝 Contributing

We welcome contributions to WealthWise! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows our coding standards and includes appropriate tests.

## 👨‍💻 Developers

WealthWise is developed and maintained by the SE 306 development team.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

© 2025 WealthWise. All Rights Reserved.