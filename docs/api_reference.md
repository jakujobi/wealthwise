# API Reference

## Overview

The WealthWise platform provides a RESTful API for accessing and managing financial data. This document provides detailed information about the available API endpoints and their usage.

## Authentication

All API requests require authentication using a token. To obtain a token, you need to log in with your credentials and receive a token in response. Include this token in the `Authorization` header of your API requests.

## Endpoints

### User Endpoints

#### Register a New User

- **URL**: `/api/users/register/`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string",
    "email": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "username": "string",
    "email": "string"
  }
  ```

#### User Login

- **URL**: `/api/users/login/`
- **Method**: `POST`
- **Description**: Log in a user and obtain an authentication token.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "token": "string"
  }
  ```

#### User Profile

- **URL**: `/api/users/profile/`
- **Method**: `GET`
- **Description**: Retrieve the profile information of the authenticated user.
- **Response**:
  ```json
  {
    "id": "integer",
    "username": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "phone_number": "string",
    "profile_picture": "string",
    "address": "string",
    "city": "string",
    "state": "string",
    "country": "string",
    "postal_code": "string"
  }
  ```

### Financial Calculators Endpoints

#### Loan Calculator

- **URL**: `/api/calculators/loan/`
- **Method**: `POST`
- **Description**: Calculate loan payments.
- **Request Body**:
  ```json
  {
    "loan_amount": "number",
    "interest_rate": "number",
    "loan_term": "integer"
  }
  ```
- **Response**:
  ```json
  {
    "monthly_payment": "number",
    "total_interest": "number"
  }
  ```

#### Mortgage Calculator

- **URL**: `/api/calculators/mortgage/`
- **Method**: `POST`
- **Description**: Calculate mortgage payments.
- **Request Body**:
  ```json
  {
    "home_price": "number",
    "down_payment": "number",
    "interest_rate": "number",
    "loan_term": "integer"
  }
  ```
- **Response**:
  ```json
  {
    "monthly_payment": "number",
    "principle_amount": "number",
    "interest_amount": "number"
  }
  ```

#### Budgeting Tool

- **URL**: `/api/calculators/budgeting/`
- **Method**: `POST`
- **Description**: Calculate budget and savings goals.
- **Request Body**:
  ```json
  {
    "fixed_income": "number",
    "variable_income": "number",
    "one_year_savings_goal": "number",
    "expenses": {
      "housing": "number",
      "taxes": "number",
      "car_payment": "number",
      "internet_phone": "number",
      "subscriptions": "number",
      "food": "number",
      "entertainment": "number",
      "personal_items": "number",
      "utilities": "number",
      "transportation": "number",
      "medical": "number",
      "misc": "number"
    }
  }
  ```
- **Response**:
  ```json
  {
    "overspend_areas": "string",
    "savings_goal_message": "string"
  }
  ```

#### Retirement Calculator

- **URL**: `/api/calculators/retirement/`
- **Method**: `POST`
- **Description**: Calculate retirement savings.
- **Request Body**:
  ```json
  {
    "current_age": "number",
    "retirement_age": "number",
    "present_savings": "number",
    "monthly_contributions": "number",
    "rate_of_return": "number",
    "retirement_goal": "number"
  }
  ```
- **Response**:
  ```json
  {
    "expected_savings": "number",
    "meet_goal": "boolean",
    "payment_to_meet_goal": "number"
  }
  ```

#### Insurance Calculator

- **URL**: `/api/calculators/insurance/`
- **Method**: `POST`
- **Description**: Calculate insurance costs.
- **Request Body**:
  ```json
  {
    "option1_cost": "number",
    "option2_cost": "number",
    "option3_cost": "number",
    "option1_coverage": "number",
    "option2_coverage": "number",
    "option3_coverage": "number",
    "accident_probability": "number",
    "accident_cost": "number"
  }
  ```
- **Response**:
  ```json
  {
    "option1_avg_cost": "number",
    "option2_avg_cost": "number",
    "option3_avg_cost": "number",
    "best_option": "string"
  }
  ```

#### Student Loan Calculator

- **URL**: `/api/calculators/student-loan/`
- **Method**: `POST`
- **Description**: Calculate student loan payments.
- **Request Body**:
  ```json
  {
    "loan_amount": "number",
    "interest_rate": "number",
    "loan_term": "integer"
  }
  ```
- **Response**:
  ```json
  {
    "monthly_payment": "number",
    "total_interest": "number",
    "total_cost": "number",
    "adjusted_term": "integer",
    "monthly_payment_adj_term": "number",
    "total_interest_adj_term": "number",
    "total_cost_adj_term": "number"
  }
  ```

#### Car Payment Calculator

- **URL**: `/api/calculators/car-payment/`
- **Method**: `POST`
- **Description**: Calculate car payment costs.
- **Request Body**:
  ```json
  {
    "loan_amount": "number",
    "interest_rate": "number",
    "down_payment": "number",
    "loan_term": "integer"
  }
  ```
- **Response**:
  ```json
  {
    "monthly_payment": "number",
    "total_interest": "number",
    "total_cost": "number",
    "adjust_double_initial_payment": "number",
    "monthly_payment_adj_pay": "number",
    "total_interest_adj_pay": "number",
    "total_cost_adj_pay": "number"
  }
  ```

### Consultation and Event Endpoints

#### Schedule a Consultation

- **URL**: `/api/schedule/consultation/`
- **Method**: `POST`
- **Description**: Schedule a consultation with a financial advisor.
- **Request Body**:
  ```json
  {
    "client_id": "integer",
    "advisor_id": "integer",
    "scheduled_date": "string",
    "status": "string"
  }
  ```
- **Response**:
  ```json
  {
    "consultation_id": "integer",
    "client_id": "integer",
    "advisor_id": "integer",
    "scheduled_date": "string",
    "status": "string"
  }
  ```

#### Register for an Event

- **URL**: `/api/schedule/event/`
- **Method**: `POST`
- **Description**: Register for a financial event.
- **Request Body**:
  ```json
  {
    "user_id": "integer",
    "title": "string",
    "description": "string",
    "event_date": "string",
    "location": "string",
    "event_type": "string"
  }
  ```
- **Response**:
  ```json
  {
    "event_id": "integer",
    "user_id": "integer",
    "registration_date": "string",
    "title": "string",
    "description": "string",
    "event_date": "string",
    "location": "string",
    "event_type": "string"
  }
  ```

## Error Handling

All API responses include an HTTP status code to indicate the success or failure of the request. In case of an error, the response will include an error message providing more details about the issue.

## Conclusion

This API reference provides an overview of the available endpoints and their usage. For more detailed information and examples, refer to the WealthWise API documentation.
