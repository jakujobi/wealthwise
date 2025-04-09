# Database Schema

This document outlines the database schema for WealthWise, including tables, relationships, and field descriptions.

## Overview

WealthWise uses PostgreSQL as its primary database. The schema consists of tables representing:

- Users and profiles
- Financial calculators and usage history
- Consultations and appointments
- Events and schedules
- Educational resources

## Entity Relationship Diagram

```
                                  +-----------------+
                                  |                 |
     +--------------------------->|     User        |<----------------------------+
     |                            |                 |                             |
     |                            +-----------------+                             |
     |                                    |                                       |
     |                                    |                                       |
     |                                    v                                       |
     |                            +-----------------+                             |
     |                            |                 |                             |
     |                            |   UserProfile   |                             |
     |                            |                 |                             |
     |                            +-----------------+                             |
     |                                    |                                       |
     |                                    |                                       |
+----+-------+                    +-------+--------+                   +----------+----+
|            |                    |                |                   |               |
| Consultation|<----------------->| FinancialTool  |<----------------->|    Event      |
|            |                    |    Usage       |                   |               |
+------------+                    +----------------+                   +---------------+
```

## Tables and Fields

### Users App

#### User (Django's built-in User model)

| Field         | Type         | Description                      |
|---------------|--------------|----------------------------------|
| id            | AutoField    | Primary key                      |
| username      | CharField    | User's username                  |
| email         | EmailField   | User's email address             |
| password      | CharField    | Hashed password                  |
| first_name    | CharField    | User's first name                |
| last_name     | CharField    | User's last name                 |
| is_active     | BooleanField | Whether user account is active   |
| is_staff      | BooleanField | Whether user is staff            |
| is_superuser  | BooleanField | Whether user is superuser        |
| date_joined   | DateTimeField| Date user joined                 |
| last_login    | DateTimeField| Date of last login               |

#### UserProfile

| Field         | Type         | Description                      |
|---------------|--------------|----------------------------------|
| user_id       | ForeignKey   | Reference to User                |
| bio           | TextField    | User biography                   |
| phone_number  | CharField    | User's phone number              |
| profile_image | ImageField   | User's profile image             |
| created_at    | DateTimeField| When profile was created         |
| updated_at    | DateTimeField| When profile was last updated    |

#### Advisor

| Field         | Type         | Description                      |
|---------------|--------------|----------------------------------|
| advisor_id    | AutoField    | Primary key                      |
| user_id       | ForeignKey   | Reference to User                |
| specialization| CharField    | Advisor's specialization         |
| experience    | IntegerField | Years of experience              |
| rating        | FloatField   | Average rating                   |
| rate_per_hour | DecimalField | Hourly rate                      |

### Calculators App

#### FinancialToolUsage

| Field         | Type         | Description                      |
|---------------|--------------|----------------------------------|
| usage_id      | AutoField    | Primary key                      |
| user_id       | ForeignKey   | Reference to UserProfile         |
| tool_type     | CharField    | Type of calculator used          |
| input_data    | JSONField    | Input data for calculation       |
| usage_date    | DateTimeField| When calculation was performed   |
| budget_for_date | DateField  | Date the budget applies to       |

### Schedule App

#### Consultation

| Field         | Type         | Description                      |
|---------------|--------------|----------------------------------|
| consultation_id | AutoField  | Primary key                      |
| client_id     | ForeignKey   | Reference to UserProfile         |
| advisor_id    | ForeignKey   | Reference to Advisor             |
| scheduled_date| DateTimeField| When consultation is scheduled   |
| status        | CharField    | Status (scheduled, completed, cancelled) |
| client_rating | IntegerField | Rating given by client (1-5)     |
| session_notes | TextField    | Notes from the consultation      |

#### Event

| Field         | Type         | Description                      |
|---------------|--------------|----------------------------------|
| event_id      | AutoField    | Primary key                      |
| user_id       | ForeignKey   | Reference to UserProfile         |
| registration_date | DateTimeField | When user registered for event |
| title         | CharField    | Event title                      |
| description   | TextField    | Event description                |
| event_start_timestamp | DateTimeField | Event start time        |
| event_end_timestamp | DateTimeField | Event end time            |
| location      | CharField    | Event location                   |

### Learning App

The Learning app currently has minimal database models as it primarily serves static content. Future iterations may include models for tracking user progress, quizzes, and personalized content.

## Relationships

### One-to-One Relationships

- User to UserProfile: Each user has exactly one profile

### One-to-Many Relationships

- UserProfile to FinancialToolUsage: A user can use multiple financial tools
- UserProfile (as client) to Consultation: A user can have multiple consultations
- Advisor to Consultation: An advisor can have multiple consultations
- UserProfile to Event: A user can register for multiple events

## Indexing Strategy

The database uses indexes on the following fields for performance optimization:

- User.username and User.email (unique indexes)
- FinancialToolUsage.user_id and FinancialToolUsage.usage_date (compound index)
- Consultation.client_id and Consultation.scheduled_date (compound index)
- Consultation.advisor_id and Consultation.scheduled_date (compound index)
- Event.event_start_timestamp (for date range queries)

## Database Migrations

Database migrations are managed through Django's migration system. Migration files are stored in the `migrations` directory of each app.

To apply migrations:

```bash
python manage.py migrate
```

To create new migrations after model changes:

```bash
python manage.py makemigrations
```

## Data Access Patterns

### Common Queries

1. Retrieve a user's profile:
   ```python
   profile = UserProfile.objects.get(user=user)
   ```

2. Get a user's financial tool usage history:
   ```python
   history = FinancialToolUsage.objects.filter(user_id=profile).order_by('-usage_date')
   ```

3. Get upcoming consultations for a client:
   ```python
   consultations = Consultation.objects.filter(
       client_id=profile,
       scheduled_date__gte=timezone.now(),
       status='scheduled'
   ).order_by('scheduled_date')
   ```

4. Get upcoming events:
   ```python
   events = Event.objects.filter(
       event_start_timestamp__gte=timezone.now()
   ).order_by('event_start_timestamp')
   ```

## Next Steps

- [User Module](./user-module.md) - Learn more about the user management
- [Calculators Module](./calculators-module.md) - Explore the financial calculators
- [Schedule Module](./schedule-module.md) - Understand consultation scheduling 